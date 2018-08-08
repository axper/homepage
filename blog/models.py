from django.db import models
from django.utils import timezone
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, IntegerBlock, URLBlock, \
    PageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index


# region Resume Blocks
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


class HomePageCardBlock(StructBlock):
    page = PageChooserBlock(required=False)
    url = URLBlock(required=False)
    content = RichTextBlock()

    class Meta:
        template = 'blog/blocks/home_page_card_block.html'
        help_text = 'One of Page or Url is required'


# endregion


# region Pages
class BaseFormattedPage(Page):

    class Meta:
        abstract = True


class HomePage(BaseFormattedPage):
    content = StreamField([
        ('link_blocks', HomePageCardBlock()),
    ])

    content_panels = BaseFormattedPage.content_panels + [
        StreamFieldPanel('content'),
    ]


class ResumePage(BaseFormattedPage):
    content = StreamField([
        ('section_block', SectionBlock()),
    ], blank=True)

    content_panels = BaseFormattedPage.content_panels + [
        StreamFieldPanel('content'),
    ]


class BlogIndexPage(BaseFormattedPage):
    # noinspection PyMethodOverriding
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blog_pages = self.get_children().live().order_by('-first_published_at')
        context['blog_pages'] = blog_pages
        return context

    subpage_types = ['blog.BlogPage']


class BlogPage(BaseFormattedPage):
    date = models.DateField("Post date", default=timezone.now)
    body = RichTextField(blank=False)

    search_fields = BaseFormattedPage.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = BaseFormattedPage.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading='Blog information'),
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
# endregion
