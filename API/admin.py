from django.contrib import admin

# Register your models here.

from .models import Product, ShoopingCart, ProductShoppingCar


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "stock", "cost", "taxes", "picture"]
    search_fields = ["name"]
    list_per_page = 10


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "user", "total_cost", "total_taxes", "products_quantity"]
    search_fields = ["status", "user"]
    list_per_page = 10


class ProductShoppingCarAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "shopping_cart", "added_quantity", "total_cost", "total_taxes", "unitary_cost"]
    search_fields = ["product", "shopping_cart"]
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(ShoopingCart, ShoppingCartAdmin)
admin.site.register(ProductShoppingCar, ProductShoppingCarAdmin)
