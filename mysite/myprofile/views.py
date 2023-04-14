from django.contrib import messages
from django.shortcuts import render, redirect

from myauth.models import UserProfile
from myprofile.forms import UserProfileForm


def personal_account(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        context = {
            "profile": profile,
        }
        return render(request, 'myprofile/account.html', context=context)
    return redirect("myauth:login")


def profile_view(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password1 = form.cleaned_data["password1"]
            phone_number = form.cleaned_data["phone_number"]
            image = form.cleaned_data["image"]
            print(username, email, password, password1, phone_number, image)
            messages.success(request, "Профиль успешно сохранен")

    return render(request, "myauth/register.html", {'form': form, 'messages': messages})


def cart_view(request):
    return render(request, 'myprofile/cart.html')