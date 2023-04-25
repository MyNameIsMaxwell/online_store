from django.urls import path

from myorder.views import order_view, order_history, order_details

app_name = "myorder"

urlpatterns = [
    path("", order_history, name="order-history"),
    path("create/", order_view, name="order"),
    path("<int:order_id>", order_details, name="order-details"),
    ]