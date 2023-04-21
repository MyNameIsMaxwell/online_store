from django import template
from django.db.models import Max

from mycatalog.models import Product

register = template.Library()


@register.filter(name='max')
def max_value(initial):
    max_value = int(Product.objects.order_by('-price').first().price)
    return max_value
