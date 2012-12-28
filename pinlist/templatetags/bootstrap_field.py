__author__ = 'jxl'

from django import template

register = template.Library()

@register.inclusion_tag('tags/bootstrap_field.html')
def bootstrap_field(field):
    return {'field': field}

