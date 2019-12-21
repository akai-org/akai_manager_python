from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ArticleSerializer, UpdateArticleListSerializer, ArticleListSerializer
from .models import Article


class ArticleSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = UpdateArticleListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'create': IsAuthenticated,
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, **kwargs):
        queryset = Article.objects.all().order_by('-created_at')
        if request.user.is_authenticated and request.user.groups.filter(name='Publisher').exists():
            self.pagination_class = ArticleSetPagination
            serializer = ArticleListSerializer(queryset, many=True)
        else:
            self.pagination_class = None
            serializer = UpdateArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('manage_articles'):
            serializer = ArticleListSerializer(data=request.data)
            return Response(serializer.data)
        else:
            response = {'error': 'User has no permissions to perform this action'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if self.request.query_params.get('noescape'):
            serializer = ArticleSerializer(article, context={'escape': False})
        else:
            serializer = ArticleSerializer(article, context={'escape': True})
        return Response(serializer.data)

    def partial_update(self, request, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated and request.user.has_perm('manage_articles'):
            serializer = ArticleListSerializer(article, data=request.data)
            return Response(serializer.data)
        else:
            response = {'error': 'User has no permissions to perform this action'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated and request.user.has_perm('manage_articles'):
            article.delete()
            response = {'success': 'Article deleted successfully'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'error': 'User has no permissions to perform this action'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
