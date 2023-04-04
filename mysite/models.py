from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCompany(models.Model):
    name = models.CharField(max_length=50)


def product_directory_path(instance, filename):
    return 'product_{0}/{1}'.format(instance.product.id, filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=product_directory_path, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL)
    seller = models.ForeignKey(ProductCompany, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return 'profile_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Avatar')

    def __str__(self):
        return self.user.username


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [('Card', 'Онлайн картой'), ('Other', 'Онлайн со случайного чужого счета')]
    DELIVERY_TYPE_CHOICES = [('Common', 'Обычная доставка'), ('Express', 'Экспресс доставка')]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES, default='Common')  # .label, чтобы вывести значение
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='Card')
    summary_price = models.DecimalField(max_digits=7, decimal_places=2)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
