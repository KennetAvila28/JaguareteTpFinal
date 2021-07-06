from django import template

register = template.Library()


@register.filter
def userdetails(value):
    return f'../media/{value}'



