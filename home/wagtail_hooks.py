from wagtail import hooks
from django.templatetags.static import static
from django.utils.html import format_html
import logging

logger = logging.getLogger(__name__)

@hooks.register('insert_global_admin_js')
def global_admin_js():
    # print("🔥 正确的 wagtail_hooks.py 被加载！")
    return format_html(
        '<script src="{}"></script><link rel="stylesheet" href="{}">',
        static('js/custom-logo.js'),
        static('css/custom-admin.css'),
    )
