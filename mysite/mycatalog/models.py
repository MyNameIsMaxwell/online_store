from _decimal import Decimal
from unicodedata import category

from django.db import models

from myauth.models import UserProfile


class ProductTags(models.Model):
    class Meta:
        ordering = ['name', ]
        verbose_name = "Тег"
        verbose_name_plural = "Тэги"

    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=100, verbose_name="Название")
    active = models.BooleanField(default=True, verbose_name="Активна")
    chosen = models.BooleanField(default=False, verbose_name="Избранный")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


# class ProductCompany(models.Model):
#     name = models.CharField(max_length=50)


def product_directory_path(instance, filename):
    return 'product_{0}/{1}'.format(instance.product.id, filename)


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL, verbose_name="Категория")
    tags = models.ManyToManyField(ProductTags, related_name='tags', verbose_name="Тэг")
    # seller = models.ForeignKey(ProductCompany, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True, verbose_name="Активен")
    limited = models.BooleanField(default=False, verbose_name="Ограниченный тираж")
    count = models.PositiveIntegerField(default=0)
    purchases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image", verbose_name="Продукт")
    image = models.ImageField(upload_to=product_directory_path, blank=True, verbose_name="Изображение")


class ProductReview(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Продукт")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    # rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания")
