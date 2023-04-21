from django.shortcuts import render

from myauth.models import UserProfile


def order_view(request):
    return render(request, 'myorder/order.html')


def order_history(request):
    orders = UserProfile.objects.get(user=request.user)
    return render(request, 'myorder/historyorder.html', {'profile': orders})
