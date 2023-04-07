from django.shortcuts import render


def card_payment(request):
    return render(request, 'mypayment/payment.html')


def other_payment(request):
    return render(request, 'mypayment/paymentsomeone.html')


def progress_payment(request):
    return render(request, 'mypayment/progressPayment.html')

