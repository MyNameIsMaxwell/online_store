from django.shortcuts import render


def order_view(request):
    return render(request, 'myorder/order.html')


def order_history(request):
    return render(request, 'myorder/historyorder.html')
