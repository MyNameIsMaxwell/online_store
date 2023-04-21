from django import template

register = template.Library()


@register.filter(name='split')
def split(str, key):
    return str.split(key)


@register.filter(name='sum')
def sum_price(products):
    summary_price = sum(products.values_list('product__price', flat=True))
    print()
    return summary_price