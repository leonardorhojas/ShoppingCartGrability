from rest_framework import serializers
from .models import ShoopingCart, Product, ProductShoppingCar, Profile
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "quantity"]
        extra_kwargs = {'name': {'required': True}}


class ShoppingCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = ShoopingCart
        fields = ["id", "products"]
        extra_kwargs = {'products': {'required': False}}


class ProductShoppingCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShoppingCar
        fields = ["product", "shoppingcart", "added_products"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'shoppingcart']