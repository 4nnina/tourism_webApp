from django import template

register = template.Library()

@register.filter
def make_break(value):
    return value.replace("\\n", "<br>")