from django.forms import model_to_dict
from django.http import QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse

from myauth.models import UserProfile
from myorder.models import Order
from myprofile.forms import UserProfileForm, DeliveryOrderForm, PaymentOrderForm


def order_view(request):
    profile = UserProfile.objects.get(user=request.user)
    params = QueryDict(mutable=True)
    # profile_dict = model_to_dict(profile)
    # print(params)
    form_delivery = DeliveryOrderForm
    form_auth = UserProfileForm(instance=profile)
    form_payment = PaymentOrderForm
    # if request.method == 'POST':
        # return reverse('myorder:order', kwargs={'step':})
    print(request.GET)
    print(request.POST)
    # print(request.POST.get('step'))
    context = {
        'form1': form_auth,
        'form2': form_delivery,
        'form3': form_payment,
    }
    return render(request, 'myorder/order.html', context=context)


def order_history(request):
    orders = UserProfile.objects.get(user=request.user)
    return render(request, 'myorder/historyorder.html', {'profile': orders})


def order_details(request, order_id):
    order = Order.objects.prefetch_related('items').prefetch_related('items__product').prefetch_related('payment').get(id=order_id)
    return render(request, 'myorder/oneorder.html', {'order': order})
