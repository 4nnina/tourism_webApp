from django import template

register = template.Library()

@register.filter
def make_break(value):
    return value.replace("\\n", "<br>")

@register.filter
def check(select, id):
    if select[int(id)]:
        return True
    else:
        return False