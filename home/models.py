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
        HelpPanel(content=mark_safe("<i>Button Title</i>")),
        FieldPanel('title'),

        HelpPanel(content=mark_safe("<i>Button Link</i>")),
        FieldPanel('url'),

        HelpPanel(content=mark_safe("<i>Button logo or icon</i>")),
        FieldPanel('logo'),
    ]

# 主链接
class HomeLink(ClusterableModel):
    homepage = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    # icon_class = models.CharField(max_length=100, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    url = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL)

    panels = [
        FieldPanel('title'),

        # HelpPanel(content=mark_safe("<img src='/static/images/prefix.jpg' alt='说明图片'><br/><i>Get (Icon class) <a href='https://icon-sets.iconify.design/' target='_blank' rel='noopener noreferrer'>Click here</a> *icon set ( Huge Icons )</i>")),
        # FieldPanel('icon_class'),

        HelpPanel(content=mark_safe(
            '<a href="#" onclick="window.open(\'/static/images/icon_tip.jpg\', \'_blank\', \'width=800,height=600\'); return false;">'
            '<img class="help-img" src="/static/images/howtodo.jpg" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;"><span class="hugeicons--touchpad-04"></span>'
            '</a><br/>'
            '<i>Get Icon <a href="https://icon-sets.iconify.design/" target="_blank" rel="noopener noreferrer">Click here</a> *icon set ( Huge Icons )</i>'
        )),
        FieldPanel('icon'),

        HelpPanel(content=mark_safe("<i>Select the page to link when this item is clicked.</i>")),
        FieldPanel('url'),

        HelpPanel(content=mark_safe("<i>These links will appear under the main link, like Awesome and Bitfinex under Crypto.</i>")),
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
        HelpPanel(content=mark_safe(
            '<a href="#" class="help-img" onclick="window.open(\'/static/images/prefix.jpg\', \'_blank\', \'width=800,height=600\'); return false;">'
            '<img src="/static/images/howtodo.jpg" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        FieldPanel('welcome_prefix'),

        HelpPanel(content=mark_safe(
            '<a href="#" class="help-img" onclick="window.open(\'/static/images/brandname.jpg\', \'_blank\', \'width=800,height=600\'); return false;">'
            '<img src="/static/images/howtodo.jpg" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        FieldPanel('brand_name'),

        FieldPanel('intro'),

        HelpPanel(content=mark_safe(
            '<a href="#" class="help-img" onclick="window.open(\'/static/images/linkdetials.jpg\', \'_blank\', \'width=800,height=600\'); return false;">'
            '<img src="/static/images/howtodo.jpg" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        InlinePanel('links', label='Home Links'),

        # HelpPanel(content=mark_safe('<img src="/static/images/sample1.jpg" alt="说明图片">')),
        # FieldPanel("image"),
        
    ]
