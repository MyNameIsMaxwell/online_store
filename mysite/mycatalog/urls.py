from django.urls import path

from mycatalog.views import catalog_view, product_details_view, sales_view

app_name = "mycatalog"

urlpatterns = [
    path("", catalog_view, name="index"),
    path("details/", product_details_view, name="product-details"),
    path("sales/", sales_view, name="sales"),
    ]