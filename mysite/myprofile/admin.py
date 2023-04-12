from django.contrib import admin
from django.contrib.auth.models import Group

from myauth.models import UserProfile
from myprofile.models import Cart, CartItem


# class RoleInline(admin.TabularInline):
#     model = Group
#     extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # inlines = [RoleInline, ]
    list_display = "pk", "name", "email", "role"
    list_display_links = "pk", "name"
    search_fields = "name",
    ordering = "pk", "role", "name"
    fieldsets = [
        (None, {
            "fields": ("name", "role"),
        }),
        ("Profile info", {
            "fields": ("phone_number", "address", "email", "image"),
            "classes": ("wide", "collapse",),
        })
    ]


class CartItemInline(admin.TabularInline):
    model = CartItem
    ordering = "-updated_at",
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]
    list_display = "pk", "profile"
    list_display_links = "pk", "profile"
    search_fields = "pk",
    ordering = "pk",


# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.utils.translation import gettext, gettext_lazy as _
#
# admin.site.unregister(User)  # нужно что бы снять с регистрации модель User
#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = UserCreationForm.Meta.model
#         fields = '__all__'
#         field_classes = UserCreationForm.Meta.field_classes
#
#
# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     add_form = CustomUserCreationForm
#     add_fieldsets = (
#         (None, {'fields': ('username', 'password1', 'password2')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
