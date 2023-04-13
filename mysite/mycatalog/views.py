from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from myauth.models import UserProfile
from mycatalog.models import ProductCategory, Product


def catalog_view(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.filter(active=True, parent=None)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    context = {
        "products": page_products,
        "categories": categories,
    }
    return render(request, 'catalog/content-page.html', context=context)


def main_view(request):
    context = {
        "categories": ProductCategory.objects.filter(active=True, parent=None),
    }
    return render(request, 'catalog/main.html', context=context)


class ProductDetailsView(DetailView):
    template_name = 'catalog/product-details.html'
    queryset = Product.objects.\
        select_related("category").\
        prefetch_related("reviews").\
        prefetch_related("tags")
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context["profile"] = UserProfile.objects.get(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST.get("amount"))
        print(request.POST.get("product_id"))
        print(request.user)
        return redirect(request.path)


# def product_details_view(request, pk):
#     return render(request, 'catalog/product-details.html')


def sales_view(request):
    return render(request, 'catalog/sale.html')
