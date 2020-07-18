from django.db import models
from django.contrib.auth.models import User


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    # product__shopping_cart = Required('Product_ShoppingCart')


# ShoppingCart Model
class ShoopingCart(models.Model):
    user = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='ProductShoppingCar', blank=True)


# Intermediate Model Product - ShoppingCart
class ProductShoppingCar(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoppingcart = models.ForeignKey(ShoopingCart, on_delete=models.CASCADE)
    added_products = models.IntegerField(default=0)


"""class Product_ShoppingCart(models.Model):
    #    id = PrimaryKey(int, auto=True)
    shoppingcarts = models.CharField(max_length=255)
    products = models.ManyToManyField('Product', related_name='products', blank=True)
    #    product__shopping_cart = Required('Product_ShoppingCart')"""


# Customized Model for
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shoppingcart = models.OneToOneField(ShoopingCart, on_delete=models.CASCADE)

    # shoppingcart = models.ForeignKey(ShoppingCart, related_name='ShoppingCart', on_delete=models.CASCADE, )
    def __str__(self):
        return self.user.username
