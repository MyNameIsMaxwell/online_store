from django.shortcuts import render


def login_view(request):
    return render(request, 'myauth/login.html')


def register_view(request):
    return render(request, 'myauth/register.html')


def password_retrieval(request):
    return render(request, 'myauth/e-mail.html')
