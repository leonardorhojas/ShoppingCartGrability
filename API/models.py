from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Product Model
    """

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class ShoopingCart(models.Model):
    """
    ShoppingCart Model
    # CHOICES:
    #     DRAFT = "DR"
    #     PENDING = "PD"
    #     PAID = "PY"
    #     IN_PROGRESS = "IP"
    #     COMPLETED = "CP"
    #     CANCELED = "CC"
    """

    products = models.ManyToManyField(Product, through='ProductShoppingCar', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_bought_products = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    DRAFT = "DR"
    PENDING = "PD"
    PAID = "PY"
    IN_PROGRESS = "IP"
    COMPLETED = "CP"
    CANCELED = "CC"
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (IN_PROGRESS, 'In_Progress'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=DRAFT
    )




class ProductShoppingCar(models.Model):
    """
    Intermediate Model Product - ShoppingCart
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoppingcart = models.ForeignKey(ShoopingCart, on_delete=models.CASCADE)
    added_quantity = models.IntegerField(default=0)
