from rest_framework import serializers
from .models import ShoopingCart, Product, ProductShoppingCar
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "picture", "name", "stock", "cost", "taxes", "picture"]
        extra_kwargs = {'name': {'required': True}}

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance


class ShoppingCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = ShoopingCart
        fields = ["id", "user", "products", "total_cost", "total_taxes", "products_quantity"]
        extra_kwargs = {'products': {'required': False}}


def check_added_quantity(data):
    """
    Check that the added quantity doesn't be grater than quantity od the product added to the car
    :return:Not enough products
    """
    added_quantity = data['added_quantity']
    product = Product.objects.get(id=int(data["product"].id))
    if added_quantity > product.stock:
        raise serializers.ValidationError('Not enough products')
    return data


class ProductShoppingCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShoppingCar
        fields = ["product", "shopping_cart", "added_quantity", "total_cost", "total_taxes", "unitary_cost"]
        validators = [
            check_added_quantity
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
