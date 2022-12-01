from rest_framework import serializers
from .models import Cart, CartItem

class CartSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = "__all__"

        
class CartItemSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        field = "__all__"
