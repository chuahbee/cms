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
from django.templatetags.static import static

# 子链接
class HomeSubLink(models.Model):
    page = ParentalKey('HomeLink', on_delete=models.CASCADE, related_name='sublinks')
    title = models.CharField(max_length=100, help_text="Button Title")
    url = models.ForeignKey('wagtailcore.Page', null=True, on_delete=models.SET_NULL, help_text="Button Link")
    logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, help_text="Button logo or icon")
    is_visible = models.BooleanField(default=True, help_text="Show this sub link on the homepage?")

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
        FieldPanel('logo'),
        FieldPanel('is_visible'),

    ]

# 主链接
class HomeLink(ClusterableModel):
    homepage = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100, help_text="button Title")
    # icon_class = models.CharField(max_length=100, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    url = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Select the page to link when this item is clicked."
    )
    is_visible = models.BooleanField(default=True, help_text="Show this main link on the homepage?")


    panels = [
        FieldPanel('title'),

        # HelpPanel(content=mark_safe("<img src='/static/images/prefix.jpg' alt='说明图片'><br/><i>Get (Icon class) <a href='https://icon-sets.iconify.design/' target='_blank' rel='noopener noreferrer'>Click here</a> *icon set ( Huge Icons )</i>")),
        # FieldPanel('icon_class'),

        HelpPanel(content=mark_safe(
            f'<a href="#" onclick="window.open(\'{static("images/icon_tip.jpg")}\', \'_blank\', \'width=800,height=600\'); return false;">'
            f'<img class="help-img" src="{static("images/howtodo.jpg")}" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;"><span class="hugeicons--touchpad-04"></span>'
            '</a><br/>'
            '<i class="help">Get Icon <a href="https://icon-sets.iconify.design/" target="_blank" rel="noopener noreferrer">Click here</a> *icon set ( Huge Icons )</i>'
        )),
        FieldPanel('icon'),

        FieldPanel('url'),

        FieldPanel('is_visible'),

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
            f'<a href="#" class="help-img" onclick="window.open(\'{static("images/prefix.jpg")}\', \'_blank\', \'width=800,height=600\'); return false;">'
            f'<img src="{static("images/howtodo.jpg")}" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        FieldPanel('welcome_prefix'),

        HelpPanel(content=mark_safe(
            f'<a href="#" class="help-img" onclick="window.open(\'{static("images/brandname.jpg")}\', \'_blank\', \'width=800,height=600\'); return false;">'
            f'<img src="{static("images/howtodo.jpg")}" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        FieldPanel('brand_name'),

        FieldPanel('intro'),

        HelpPanel(content=mark_safe(
            f'<a href="#" class="help-img" onclick="window.open(\'{static("images/linkdetials.jpg")}\', \'_blank\', \'width=800,height=600\'); return false;">'
            f'<img src="{static("images/howtodo.jpg")}" alt="说明图片" style="width:40px; height:40px; border:1px solid #ccc;">'
            '<span class="hugeicons--touchpad-04"></span></a>'
        )),
        InlinePanel('links', label='Home Links'),

        # HelpPanel(content=mark_safe('<img src="/static/images/sample1.jpg" alt="说明图片">')),
        # FieldPanel("image"),
        
    ]
