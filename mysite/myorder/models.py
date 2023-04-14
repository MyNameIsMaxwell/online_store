from django.core.validators import MinValueValidator
from django.db import models

from myauth.models import UserProfile
from mycatalog.models import Product


class Order(models.Model):
    class Meta:
        ordering = ["-created_at", "-status"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    DELIVERY_TYPE_CHOICES = [('Common', 'Обычная доставка'), ('Express', 'Экспресс доставка')]
    ORDER_STATUS = [('Not paid', 'Не оплачен'), ('Paid', 'Оплачен'), ('Delivery', 'Доставляется'), ('Awaiting', 'Ожидает выдачи'), ('Done', 'Выдан')]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='order', verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES, default='Common', verbose_name="Тип доставки")  # .label, чтобы вывести значение
    city = models.CharField(max_length=60, verbose_name="Город")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    status = models.CharField(max_length=15, choices=ORDER_STATUS, default='Not paid', verbose_name="Статус доставки")

    def __str__(self):
        return f"{self.user.name}{self.pk}"


class OrderItem(models.Model):
    class Meta:
        verbose_name = "Продукт заказа"
        verbose_name_plural = "Продукты заказа"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveSmallIntegerField(default=1,
                                                validators=[MinValueValidator(1)],
                                                verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name}/{self.order.pk}"