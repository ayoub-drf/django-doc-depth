# myapp/templatetags/my_tags.py
from django import template

register = template.Library()

@register.simple_tag
def add_numbers(a, b):
    return a + b

@register.simple_tag
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")

register.filter("cut", cut)

@register.simple_tag
def add_upper(v):
    return v.upper()