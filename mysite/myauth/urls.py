from django.urls import path

from myauth.views import login_view, register_view, password_retrieval, MyLogoutView
from mycatalog.views import main_view

app_name = "myauth"

urlpatterns = [
    path("", main_view, name="main"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("retrieval/", password_retrieval, name="password-retrieval"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    ]