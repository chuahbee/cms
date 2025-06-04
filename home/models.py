from django.db import models

from wagtail.models import Page
# from wagtail.fields import PageChooserBlock
from portfolio.models import P2PIndexPage, CreditCardsIndexPage, CryptoIndexPage
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, HelpPanel
from wagtail import blocks
from wagtail.images.models import Image
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.fields import StreamBlock
from wagtail.snippets.models import register_snippet
from django.utils.safestring import mark_safe

# 子链接
class HomeSubLink(models.Model):
    page = ParentalKey('HomeLink', on_delete=models.CASCADE, related_name='sublinks')
    title = models.CharField(max_length=100)
    url = models.ForeignKey('wagtailcore.Page', null=True, on_delete=models.SET_NULL)
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL)

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
        FieldPanel('logo'),
    ]

# 主链接
class HomeLink(ClusterableModel):
    homepage = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True)
    url = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL)

    panels = [
        FieldPanel('title'),
        FieldPanel('icon_class'),
        FieldPanel('url'),
        InlinePanel('sublinks', label='Sub Links'),
    ]

class HomePage(Page):
    intro = RichTextField(blank=True) 
    welcome_prefix = models.CharField(max_length=100, default="Welcome to", blank=True)
    brand_name = models.CharField(max_length=100, default="AWEPAY")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        HelpPanel(content=mark_safe('<img src="/static/images/prefix.jpg" alt="说明图片">')),
        FieldPanel('welcome_prefix'),

        HelpPanel(content=mark_safe('<img src="/static/images/brandname.jpg" alt="说明图片">')),
        FieldPanel('brand_name'),

        FieldPanel('intro'),

        HelpPanel(content=mark_safe('<img src="/static/images/linkdetials.jpg" alt="说明图片">')),
        InlinePanel('links', label='Home Links'),

        # HelpPanel(content=mark_safe('<img src="/static/images/sample1.jpg" alt="说明图片">')),
        # FieldPanel("image"),
        
    ]
