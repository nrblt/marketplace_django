from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category
from .serializers import CategoryProductSerializer, CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def retrieve(self, request, pk):
        category = self.queryset.get(pk=pk)
        serializer = CategoryProductSerializer(category, many=False)
        return Response(serializer.data)
