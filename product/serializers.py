from rest_framework import serializers

from .models import Product
from comment.serializers import CommentSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")
class ProductCommentSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = "name", "category", "size","brand", "type", "gender","price", "count", "material","description", "color", "created_at","likes", "dislikes", "comment_set"
