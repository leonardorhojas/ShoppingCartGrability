from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from django.core.validators import MinValueValidator

from .signals import post_save_product_shoppingcar, post_delete_product_shoppingcar, pre_save_product_shoppingcar


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


class Product(models.Model):
    """
    Product Model
    """
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    picture = models.ImageField(default='default.png')

    def __str__(self):
        return self.name


class ShoopingCart(models.Model):
    """
    ShoppingCart Model
    # CHOICES:
    #     DRAFT = "An order that still is pending for checkout"
    #     PENDING = "An order that already has checkout, but it's pending for payment"
    #     PAID = " An order already paid, but is pending to start .."
    #     IN_PROGRESS = "IP"
    #     COMPLETED = "CP"
    #     CANCELED = "CC"
    """
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=DRAFT
    )
    products = models.ManyToManyField(Product, through='ProductShoppingCar', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    products_quantity = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return 'Shoppingcart: ' + str(self.id) + ', User: ' + str(self.user)


class ProductShoppingCar(models.Model):
    """
    Intermediate Model Product - ShoppingCart
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoopingCart, on_delete=models.CASCADE)
    added_quantity = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    total_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    unitary_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    unitary_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        """
        Update model values before update database values
        :param args:
        :param kwargs:
        :return:
        """
        self.unitary_cost = self.product.cost
        self.unitary_taxes = self.product.taxes
        self.total_cost = self.unitary_cost * self.added_quantity
        self.total_taxes = self.product.taxes * self.added_quantity

        super(ProductShoppingCar, self).save(*args, **kwargs)


post_save.connect(post_save_product_shoppingcar, sender=ProductShoppingCar)
post_delete.connect(post_delete_product_shoppingcar, sender=ProductShoppingCar)
pre_save.connect(pre_save_product_shoppingcar, sender=ProductShoppingCar)

