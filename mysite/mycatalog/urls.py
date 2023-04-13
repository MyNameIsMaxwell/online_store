from django.urls import path

from mycatalog.views import catalog_view, ProductDetailsView, sales_view

app_name = "mycatalog"

urlpatterns = [
    path("", catalog_view, name="catalog"),
    path("details/<int:pk>", ProductDetailsView.as_view(), name="product-details"),
    path("sales/", sales_view, name="sales"),
    ]