from django import template

register = template.Library()


@register.filter
def modImage(value):
    return f'../../media/{value}'
