from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .serializers import UserSerializer, ProductSerializer, ShoppingCartSerializer, ProductShoppingCarSerializer, \
    ProfileSerializer
from .models import Product, ShoopingCart, ProductShoppingCar, Profile


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoopingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class ProductShoppingCarViewSet(viewsets.ModelViewSet):
    queryset = ProductShoppingCar.objects.all()
    serializer_class = ProductShoppingCarSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
