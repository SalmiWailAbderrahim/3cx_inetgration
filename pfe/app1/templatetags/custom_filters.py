from django import template

register = template.Library()

@register.filter
def add_five(value):
    try:
        return int(value) + 5
    except (ValueError, TypeError):
        return value
