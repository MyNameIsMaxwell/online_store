from django.contrib import admin

from mypayment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = "pk", "order", "status"
    list_display_links = "pk", "order"
    search_fields = "order",
    ordering = "status",
