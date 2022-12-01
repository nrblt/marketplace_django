from rest_framework import filters, viewsets, status
from django.contrib.auth.decorators import login_required
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwarg):
        user = request.user
        if user.is_anonymous:
            raise NotAuthenticated("Please authenticate")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if self.queryset.filter(user=user,product=serializer.validated_data['product']).exists:
                raise PermissionDenied("You already wrote comment on this product")
            comment = Comment(user=user, title=serializer.validated_data['title'], 
            product=serializer.validated_data['product'], 
            rating=serializer.validated_data['rating'])
            comment.save()
            resp = self.serializer_class(comment)
            return Response(resp.data, status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = request.user
        if user.is_anonymous:
            raise NotAuthenticated("Please authenticate")
        comment = get_object_or_404(Comment, pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            comment.text = serializer.validated_data['text']
            comment.save()
            serializer = self.serializer_class(comment)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
