from django import template

register = template.Library()

censor_filter = ['Fuck', 'Bullshit', 'Dick', 'Редиска']


@register.filter(name='censor')
def censor(value):
    for a in censor_filter:
        value = value.replace(a, a[0:2] + '*' * len(a))
    else:
        raise ValueError('censored')
    return value
