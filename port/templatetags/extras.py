from django import template

register = template.Library()

@register.filter(name='getVal')
def getVal(dict, key):
    return dict.get(key)