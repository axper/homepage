from django.db import models
from django.utils import timezone
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.blocks import StructBlock, RichTextBlock, URLBlock, \
    PageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.search import index


# region Blocks
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


class Home(BaseFormattedPage):
    content = StreamField([
        ('link_blocks', HomePageCardBlock()),
    ])

    content_panels = BaseFormattedPage.content_panels + [
        StreamFieldPanel('content'),
    ]


class BlogIndex(BaseFormattedPage):
    banner = models.ImageField(blank=True)

    # noinspection PyMethodOverriding
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndex, self).get_context(request)
        blog_pages = self.get_children().live().order_by('-first_published_at')
        context['blog_pages'] = blog_pages
        return context

    content_panels = BaseFormattedPage.content_panels + [
        FieldPanel('banner'),
    ]
    subpage_types = ['blog.Blog']


class Blog(BaseFormattedPage):
    date = models.DateField('Post date', default=timezone.now)
    banner = models.ImageField(blank=True)
    body = RichTextField(blank=False)

    search_fields = BaseFormattedPage.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = BaseFormattedPage.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('banner'),
        ], heading='Blog information'),
        FieldPanel('body', classname='full'),
    ]

    parent_page_types = ['blog.BlogIndex']
    subpage_types = []


class Map(BaseFormattedPage):
    template = 'carav/map.html'
    banner = models.ImageField(blank=True)

    content_panels = BaseFormattedPage.content_panels + [
        FieldPanel('banner'),
    ]

    parent_page_types = ['blog.Home']
    subpage_types = []
# endregion
