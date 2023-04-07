from django.urls import path

from myorder.views import order_view, order_history

app_name = "myorder"

urlpatterns = [
    path("", order_history, name="order-history"),
    path("create/", order_view, name="order"),
    ]