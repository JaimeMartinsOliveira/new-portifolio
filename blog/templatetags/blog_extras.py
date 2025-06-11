# blog/templatetags/blog_extras.py
import markdown
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(value):
    return mark_safe(markdown.markdown(value, extensions=['markdown.extensions.fenced_code']))