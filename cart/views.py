from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.exceptions import (ValidationError)
from rest_framework.viewsets import (ReadOnlyModelViewSet,
                                     ViewSet)
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartItemSeriailzer, CartSeriazlier
from rest_framework import status

# Create your views here.

class CartItemViewSet(ReadOnlyModelViewSet, ViewSet):
    model = CartItem
    serializer_class = CartItemSeriailzer

    @method_decorator(login_required)
    def create(self, request):
        user = request.user
        cart = get_object_or_404(Cart, owner=user)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if(serializer['count']<=0):
                raise ValidationError("Quantity must be greater than 0")
            cart_item = self.model.objects.create(product_id=serializer['product'], count=serializer['count'], cart=cart)
            cart_item.save()
            cart.total_price = cart.total_price + cart_item.count*cart_item.product.price
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
