from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Product Model
    """

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    # product__shopping_cart = Required('Product_ShoppingCart')
    total_cost = models.IntegerField(default=0)
    total_taxes = models.IntegerField(default=0)


class ShoopingCart(models.Model):
    """
    ShoppingCart Model
    """

    products = models.ManyToManyField(Product, through='ProductShoppingCar', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.IntegerField(default=0)
    total_taxes = models.IntegerField(default=0)
    total_bought_products = models.IntegerField(default=0)

class ProductShoppingCar(models.Model):
    """
    Intermediate Model Product - ShoppingCart
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoppingcart = models.ForeignKey(ShoopingCart, on_delete=models.CASCADE)
    added_quantity = models.IntegerField(default=0)
