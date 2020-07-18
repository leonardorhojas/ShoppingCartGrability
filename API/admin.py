from django.contrib import admin

# Register your models here.

from .models import Product, ShoopingCart, ProductShoppingCar


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class ShoppingCartAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShoopingCart, ShoppingCartAdmin)


class ProductShoppingCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductShoppingCar, ProductShoppingCarAdmin)