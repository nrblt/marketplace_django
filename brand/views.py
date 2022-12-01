from django.shortcuts import render
from .models import Brand
from .serializers import BrandSerializer, BrandProductSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from product.models import Product
# Create your views here.

class BrandViewSet(ReadOnlyModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def retrieve(self, request, pk):
        brand = self.queryset.get(pk=pk)
        serializer = BrandProductSerializer(brand, many=False)  
        return Response(serializer.data)