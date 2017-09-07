from django import forms
from django.db import models
from django.db.models import TextField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, IntegerBlock, URLBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet


class PortfolioCardBlock(StructBlock):
    id = CharBlock(required=False)
    title = CharBlock()
    link = URLBlock()
    image = ImageChooserBlock()
    content = RichTextBlock()

    class Meta:
        template = 'blog/blocks/portfolio_card_block.html'


class SmallGridBlock(StructBlock):
    dividend = IntegerBlock(default=1)
    divisor = IntegerBlock(default=2)
    content = StreamBlock([
        ('card_block', PortfolioCardBlock(blank=True)),
    ])

    class Meta:
        template = 'blog/blocks/small_grid_block.html'


class DescriptionListItemBlock(StructBlock):
    data_title = CharBlock()
    data_definition = CharBlock()

    class Meta:
        template = 'blog/blocks/description_list_item_block.html'


class DescriptionListBlock(StructBlock):
    content = StreamBlock([
        ('description_item_block', DescriptionListItemBlock()),
    ])

    class Meta:
        template = 'blog/blocks/description_list_block.html'


class DownloadButtonBlock(StructBlock):
    url = URLBlock()
    text = CharBlock()

    class Meta:
        template = 'blog/blocks/download_button_block.html'


class BaseSectionBlock(StructBlock):
    id = CharBlock(required=False)
    title = CharBlock()
    content_blocks = [
        ('rich_text', RichTextBlock(blank=True)),
        ('small_grid_block', SmallGridBlock(blank=True)),
        ('description_list_block', DescriptionListBlock(blank=True)),
        ('download_button_block', DownloadButtonBlock(blank=True)),
    ]


class H4WithIdBlock(BaseSectionBlock):
    class Meta:
        template = 'blog/blocks/h4_with_id_block.html'


class H3WithIdBlock(BaseSectionBlock):
    # noinspection PyTypeChecker
    content = StreamBlock(BaseSectionBlock.content_blocks + [
        ('h4_section_block', H4WithIdBlock()),
    ])

    class Meta:
        template = 'blog/blocks/h3_with_id_block.html'


class SectionBlock(BaseSectionBlock):
    # noinspection PyTypeChecker
    content = StreamBlock(BaseSectionBlock.content_blocks + [
        ('h3_section_block', H3WithIdBlock()),
    ])

    class Meta:
        template = 'blog/blocks/section_block.html'


class ResumePage(Page):
    name = TextField(default='Name Surname')
    sub_heading = TextField(default='Highly trained monkey')
    sub_sub_heading = TextField(default='Also a programmer')
    body = StreamField([
        ('section_block', SectionBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('sub_heading'),
        FieldPanel('sub_sub_heading'),
        StreamFieldPanel('body'),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # noinspection PyMethodOverriding
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=False)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading='Blog information'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label='Gallery Images')
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogTagIndexPage(Page):
    # noinspection PyMethodOverriding
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name
