from django.db import models

from myorder.models import Order


class Payment(models.Model):
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    PAYMENT_METHOD_CHOICES = [('Card', 'Онлайн картой'), ('Other', 'Онлайн со случайного чужого счета')]

    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='Card')
    summary_price = models.DecimalField(max_digits=7, decimal_places=2)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

