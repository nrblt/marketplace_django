from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Brand
from product.serializers import ProductSerializer

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("__all__")


class BrandProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ("name", "product_set")
