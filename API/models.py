from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Product Model
    """

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    # product__shopping_cart = Required('Product_ShoppingCart')


class ShoopingCart(models.Model):
    """
    ShoppingCart Model
    """

    user = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='ProductShoppingCar', blank=True)


class ProductShoppingCar(models.Model):
    """
    Intermediate Model Product - ShoppingCart
    """

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
