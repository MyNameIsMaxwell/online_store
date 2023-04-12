from django.contrib import admin

from myorder.models import Order, OrderItem
from mypayment.models import Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_select_related = ["product"]
    extra = 1


class PaymentInline(admin.TabularInline):
    model = Payment
    fields = "status",
    readonly_fields = ["status"]
    can_delete = False


@admin.register(Order)
class Order(admin.ModelAdmin):
    inlines = [OrderItemInline, PaymentInline]
    list_display = "pk", "user", "created_at", "updated_at", "status"
    list_display_links = "pk", "user"
    ordering = "status", "-created_at",
    search_fields = "pk", "user"


# @admin.register(OrderItem)
# class OrderItem(admin.ModelAdmin):
#     list_display = "order", "product"
#     ordering = "-order",
