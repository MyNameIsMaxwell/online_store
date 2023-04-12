from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from myauth.forms import RegisterForm, LoginForm
from myauth.models import UserProfile


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect(reverse('myauth:main'))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # username = UserProfile.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("myauth:main"))
            else:
                messages.error(request, "Неправильный логин или пароль")
        else:
            messages.error(request, "Неправильный логин или пароль")
    return render(request, "myauth/login.html", {"form": form})


# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = "myauth/register.html"
#     success_url = reverse_lazy("myauth:main")
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         # UserProfile.objects.create(user=self.object)
#         username = form.cleaned_data["name"]
#         email = form.cleaned_data["email"]
#         password = form.cleaned_data["pass"]
#         print(username, email, password)
#         # user = authenticate(
#         #     self.request,
#         #     username=username,
#         #     password=password,
#         # )
#         # login(request=self.request, user=user)
#         return response


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = User.objects.create(username=email)
                user.set_password(password)
                user.save()
                UserProfile.objects.create(user=user, name=username, email=email)
                user = authenticate(
                    request,
                    username=email,
                    password=password,
                )
                login(request=request, user=user)
                return redirect(reverse("myauth:main"))
            except IntegrityError:
                messages.error(request, "Пользователь уже существует!")
    return render(request, "myauth/register.html", {'form': form})
        # user = authenticate(
        #     self.request,
        #     username=username,
        #     password=password,
        # )
        # login(request=self.request, user=user)


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


def password_retrieval(request):
    return render(request, 'myauth/e-mail.html')
