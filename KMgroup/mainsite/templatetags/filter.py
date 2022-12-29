from django import template

register = template.Library()
@register.filter(name='isoweekday')
def isoweekday(value):
    return value.isoweekday()