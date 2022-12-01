from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from .models import Dislike, Like, Product
from .serializers import ProductCommentSerializer, ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def retrieve(self, request, pk):
        product = self.queryset.get(pk=pk)
        serializer = ProductCommentSerializer(product, many=False)
        return Response(serializer.data)

class LikesViewSet(ViewSet):
    queryset = Like.objects.all()

    @method_decorator(login_required)
    @action(methods=['get'], detail=True)
    def like(self, request, pk=None):
        like, created = self.queryset.get_or_create(product_id=pk, user=request.user)
        dislike = Dislike.objects.filter(product_id=pk, user=request.user)
        if dislike:
            like.product.dislikes -= 1
            like.product.save()
            dislike.delete()
        if not created: 
            like.product.likes -= 1
            like.product.save()
            like.delete()

        return Response({"likes":like.product.likes,"dislikes":like.product.dislikes},status=status.HTTP_200_OK)


class DislikesViewSet(ViewSet):    
    queryset = Dislike.objects.all()

    @method_decorator(login_required)
    @action(methods=['get'], detail=True)
    def dislike(self, request, pk=None):
        dislike, created = self.queryset.get_or_create(product_id=pk, user=request.user)
        like = Like.objects.filter(product_id=pk, user=request.user)
        if like:
            dislike.product.likes -= 1
            dislike.product.save()
            like.delete()
        if not created: 
            dislike.product.dislikes -= 1
            dislike.product.save()
            dislike.delete()
        return Response({"likes":dislike.product.likes,"dislikes":dislike.product.dislikes},status=status.HTTP_200_OK)
    @action(methods=['get'], detail=False)
    def gg(self,request):
        print("asdfads")
        return Response({"asdfdas":"ASDF"},status=status.HTTP_200_OK)
