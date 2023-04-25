from django.db import models

from myorder.models import Order


class Payment(models.Model):
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    PAYMENT_METHOD_CHOICES = [('Card', 'Онлайн картой'), ('Other', 'Онлайн со случайного чужого счета')]

    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='Card', verbose_name="Способ оплаты")
    summary_price = models.DecimalField(max_digits=7, decimal_places=2, default='999.99', verbose_name="Общая стоимость")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    status = models.BooleanField(default=False, verbose_name="Статус оплаты")

    def save(self, *args, **kwargs):
        order_items = self.order.items.all()
        total_price = sum([item.quantity*item.product.price for item in order_items])
        self.summary_price = total_price
        super().save(*args, **kwargs)
