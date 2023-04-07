from django.shortcuts import render


def catalog_view(request):
    return render(request, 'catalog/content-page.html')


def main_view(request):
    return render(request, 'catalog/main.html')


def product_details_view(request):
    return render(request, 'catalog/product-details.html')


def sales_view(request):
    return render(request, 'catalog/sale.html')
