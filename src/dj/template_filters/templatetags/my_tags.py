from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)


@register.filter(name="cut", is_safe=True)
def cut(value, arg):
    return value.replace(arg, "")


@register.filter(is_safe=True)
@stringfilter
def addUpper(value):
    print("SafeString", isinstance(value, SafeString))
    return value.upper()


@register.simple_tag
def add_numbers(a, b):
    return a + b

