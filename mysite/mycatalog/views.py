from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from myauth.models import UserProfile
from mycatalog.models import ProductCategory, Product
from myorder.forms import SortForm


def catalog_view(request):
    categories = ProductCategory.objects.filter(active=True, parent=None)
    products = Product.objects.all()
    sort_by = request.GET.get('sort_by')
    params = QueryDict(mutable=True)
    print(params.urlencode())

    page_number = request.GET.get('page')
    form = SortForm(initial={
        'available': True,
    })

    if request.method == 'GET' and request.GET.get('sort_by'):
        if sort_by == 'price':
            products = Product.objects.order_by('-price')
        elif sort_by == '-price':
            products = Product.objects.order_by('price')
        elif sort_by == 'reviews':
            products = Product.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews').distinct()
        elif sort_by == '-reviews':
            products = Product.objects.annotate(num_reviews=Count('reviews')).order_by('num_reviews').distinct()
        elif sort_by == 'date':
            products = Product.objects.order_by('-created_at')
        elif sort_by == '-date':
            products = Product.objects.order_by('created_at')
        else:
            # тут выставить по популярности
            products = Product.objects.all()
        params['sort_by'] = sort_by
            # return redirect('{}?{}'.format(reverse('mycatalog:catalog'), params.urlencode()))
    print(request.GET)
    print(request.POST)

    if request.method == 'POST':
        form = SortForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            available = form.cleaned_data['available']
            price = request.POST.get('price')
            print(name, available, price)
            if name:
                params['name'] = name.lower()
            if available:
                params['available'] = available
            params['price'] = price
            page_number = '1'

    if request.method == 'GET' and 'price' in request.GET:
        name = request.GET.get('name')
        available = request.GET.get('available')
        price = request.GET.get('price')

        form = SortForm(initial={
            'name': name,
            'available': available,
            'price': price
        })
        if name:
            params['name'] = name.lower()
        if available:
            params['available'] = available
        params['price'] = price
    print(params)

    paginator = Paginator(products, 8)
    page_products = paginator.get_page(page_number)

    context = {
        "products": page_products,
        "form": form,
        "categories": categories,
        "params": params,
    }

    return render(request, 'catalog/content-page.html', context=context)


def main_view(request):
    selected_category = ProductCategory.objects.filter(chosen=True)[:3]
    popular_products = Product.objects.order_by('-id', '-purchases')[:8]
    limited_products = Product.objects.filter(limited=True)[:16]
    context = {
        "categories": ProductCategory.objects.filter(active=True, parent=None),
        "selected_category": selected_category,
        "popular_products": popular_products,
        "limited_products": limited_products,
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
        # context['add_to_cart_form'] = AddToCartForm()
        context["profile"] = UserProfile.objects.get(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        if "add_to_cart" in request.POST:
            # add_to_cart_form = AddToCartForm(request.POST)
            # if add_to_cart_form.is_valid():
            print(request.POST.get("amount"))
            print(request.POST.get("product_id"))
            print(request.user)

        elif "submit_review" in request.POST:
            print(request.POST)
            print(request.POST.get("review"))
            print(request.POST.get("product_id"))
            print(request.user)
        return redirect(request.path)


# def product_details_view(request, pk):
#     return render(request, 'catalog/product-details.html')


def sales_view(request):
    return render(request, 'catalog/sale.html')
