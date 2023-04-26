from django import template
from django.db.models import Max, Min

from mycatalog.models import Product

register = template.Library()


@register.filter(name='max')
def max_value(initial):
    max_value = int(Product.objects.order_by('-price').first().price)
    return max_value


@register.filter(name='min')
def min_value(category):
    # min_value = Product.objects.filter(category=category).aggregate(Min("price"))
    min_value = int(Product.objects.filter(category=category).order_by('price').first().price)
    return min_value
