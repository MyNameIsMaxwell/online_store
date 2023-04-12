from django.shortcuts import render

from mycatalog.models import ProductCategory


def catalog_view(request):
    context = {

    }
    return render(request, 'catalog/content-page.html', context=context)


def main_view(request):
    context = {
        "categories": ProductCategory.objects.filter(active=True, parent=None),
    }
    return render(request, 'catalog/main.html', context=context)


def product_details_view(request):
    return render(request, 'catalog/product-details.html')


def sales_view(request):
    return render(request, 'catalog/sale.html')
