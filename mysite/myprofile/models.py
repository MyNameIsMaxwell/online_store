from django.core.validators import MinValueValidator
from django.db import models

from myauth.models import UserProfile
from mycatalog.models import Product


class Cart(models.Model):
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name="Профиль")

    def __str__(self):
        return self.profile.name


class CartItem(models.Model):
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Продукт корзины"
        verbose_name_plural = "Продукты корзины"

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products", verbose_name="Корзина")
    product = models.ForeignKey(Product, related_name="cart", on_delete=models.CASCADE, verbose_name="Продукт")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    quantity = models.PositiveSmallIntegerField(default=1,
                                                validators=[MinValueValidator(1)],
                                                verbose_name="Количество")

    def __str__(self):
        return f"{self.cart.pk} | {self.product.pk}"

