from django.contrib import messages
from django.shortcuts import render, redirect

from myauth.models import UserProfile
from myprofile.forms import UserProfileForm
from myprofile.models import CartItem


def personal_account(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        context = {
            "profile": profile,
        }
        return render(request, 'myprofile/account.html', context=context)
    return redirect("myauth:login")


def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=profile, initial={'image': profile.image})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password1 = form.cleaned_data["password1"]
            phone_number = form.cleaned_data["phone_number"]
            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = None
            print(image)
            print(username, email, phone_number, image, password, password1,)
            messages.success(request, "Профиль успешно сохранен")

    return render(request, "myprofile/profile.html", {'form': form, "profile": profile})


def cart_view(request):
    profile = UserProfile.objects.prefetch_related('cart__products__product').get(user=request.user)

    if request.method == "POST":
        if "create_order" in request.POST:
            for product in profile.cart.products.all():
                print(product.product.name)
        elif "delete" in request.POST:
            product_id = request.POST["delete"]
            item = profile.cart.products.get(id=product_id)
            print(item.product.name)
            # item.delete()
    return render(request, 'myprofile/cart.html', {'profile': profile})


