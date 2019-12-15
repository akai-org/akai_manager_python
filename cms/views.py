from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from .serializers import ArticleSerializer, UpdateArticleListSerializer
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = UpdateArticleListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, **kwargs):
        queryset = Article.objects.all()
        serializer = UpdateArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)