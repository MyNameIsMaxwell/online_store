from django.shortcuts import render


def personal_account(request):
    return render(request, 'myprofile/account.html')


def profile_view(request):
    return render(request, 'myprofile/profile.html')


def cart_view(request):
    return render(request, 'myprofile/cart.html')