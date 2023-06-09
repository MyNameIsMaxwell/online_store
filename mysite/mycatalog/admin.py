from django.contrib import admin

from .models import ProductCategory, Product, ProductTags, ProductImages, ProductReview


class CategoryInline(admin.TabularInline):
    model = ProductCategory
    readonly_fields = ['active']
    can_delete = False
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
    list_display = "pk", "name", "parent"
    list_display_links = "pk", "name"
    ordering = "pk",


class ProductTagsInline(admin.TabularInline):
    model = Product.tags.through
    classes = ["collapse"]
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"
    extra = 1


@admin.register(ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    inlines = [ProductTagsInline, ]
    list_display = "name",
    list_display_links = "name",

    # def get_product(self, obj):
    #     return [product.name for product in Product.tags.all()]

    #
    # fieldsets = [
    #     (None, {
    #         "fields": ("name", ),
    #     }),
    #     ("Profile info", {
    #         "fields": ("get_product", ),
    #         "classes": ("wide", "collapse",),
    #     })
    # ]


class ProductImagesInline(admin.TabularInline):
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"
    model = ProductImages
    extra = 1


@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImagesInline, ]
    list_display = "pk", "name", "category", "price", "limited"
    list_display_links = "pk", "name"
    ordering = "name", "category"
    search_fields = "pk", "name"
    list_filter = "category",
    fieldsets = [
        (None, {
            "fields": ("name", "active", "limited"),
        }),
        ("Детали", {
            "fields": ("description", "price", "category", "tags", "count", "purchases"),
            "classes": ("wide", "collapse",),
        })
    ]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = "user", "product"
    list_display_links = "user",
    verbose_name = "Отзыв"
    verbose_name_plural = "Отзывы"