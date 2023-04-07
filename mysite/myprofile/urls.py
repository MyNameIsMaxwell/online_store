from django.urls import path

from myprofile.views import personal_account, profile_view, cart_view

app_name = "myprofile"

urlpatterns = [
    path("", personal_account, name="personal-account"),
    path("profile/", profile_view, name="profile"),
    path("cart/", cart_view, name="cart"),
    ]