from django.urls import path

from mypayment.views import card_payment, other_payment, progress_payment

app_name = "mypayment"

urlpatterns = [
    path("", card_payment, name="card-payment"),
    path("other/", other_payment, name="other-payment"),
    path("progress/", progress_payment, name="progress-payment"),
    ]