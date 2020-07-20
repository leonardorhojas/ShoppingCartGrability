def update_shoppingcar(shopping_cart):
    """
    Update values of shopping cart
    :param shopping_cart:
    :return:
    """
    from .models import ProductShoppingCar

    total_cost = 0
    total_taxes = 0
    products_quantity = 0

    shoppingcart = shopping_cart
    products = ProductShoppingCar.objects.filter(shopping_cart=shoppingcart)
    # update ShoppingCart Values
    for product in products:
        total_cost += product.total_cost
        total_taxes += product.total_taxes
        products_quantity += product.added_quantity

    shoppingcart.total_cost = total_cost
    shoppingcart.total_taxes = total_taxes
    shoppingcart.products_quantity = products_quantity
    shoppingcart.save()


def pre_save_product_shoppingcar(sender, instance, **kwargs):
    """
    Signal for update task on product and shoppingcart when a product_shopping_cart is deleted
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    from .models import ProductShoppingCar

    if not instance.id:
        return

    # Update product Stock
    product = instance.product
    product_shopping_cart = ProductShoppingCar.objects.get(id=instance.id)
    product.stock = product.stock + product_shopping_cart.added_quantity
    product.save()


def post_save_product_shoppingcar(sender, instance, **kwargs):
    """
    Signal for update task on product and shoppingcart when a product_shopping_cart is deleted
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Update product Stock
    product = instance.product
    product.stock = product.stock - instance.added_quantity
    product.save()

    # Update Values of the shoppingcart
    update_shoppingcar(instance.shopping_cart)


def post_delete_product_shoppingcar(sender, instance, **kwargs):
    """
    Signal for update task on product and shoppingcart when a product_shopping_cart is deleted
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Update product Stock
    product = instance.product
    product.stock = product.stock + instance.added_quantity
    product.save()

    # Update Values of the shoppingcart
    update_shoppingcar(instance.shopping_cart)


def post_save_product_shoppingcar(sender, instance, **kwargs):
    """
    Signal for update task on product and shoppingcart when a product_shopping_cart is deleted
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Update product Stock
    product = instance.product
    product.stock = product.stock - instance.added_quantity
    product.save()

    # Update Values of the shoppingcart
    update_shoppingcar(instance.shopping_cart)
