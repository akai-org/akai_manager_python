from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ArticleSerializer, UpdateArticleListSerializer, ArticleListSerializer, TagListSerializer
from .models import Article, Tag


class ArticleSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = UpdateArticleListSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def toggle_activate(self, request, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated and request.user.has_perm('cms.manage_article'):
            article.active = not article.active
            article.save()
            return Response(status=status.HTTP_200_OK)
        else:
            response = {'error': 'User has no permissions to perform this action'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def list(self, request, **kwargs):
        queryset = Article.objects.all().order_by('-created_at')
        if request.user.is_authenticated and request.user.groups.filter(name='Publisher').exists():
            self.pagination_class = ArticleSetPagination
            serializer = ArticleListSerializer(queryset, many=True)
        else:
            queryset = queryset.filter(active=True)
            self.pagination_class = None
            serializer = UpdateArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        if request.user.is_authenticated and request.user.has_perm('cms.manage_article'):
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
        if request.user.is_authenticated and request.user.has_perm('cms.manage_article'):
            serializer = ArticleListSerializer(article, data=request.data)
            return Response(serializer.data)
        else:
            response = {'error': 'User has no permissions to perform this action'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated and request.user.has_perm('cms.manage_article'):
            article.delete()
            response = {'success': 'Article deleted successfully'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'error': 'User has no permissions to perform this action',
                        'perm': request.user.has_perm('cms.manage_article')}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(login_required, name="dispatch")
class ArticleIndexView(TemplateView):
    template_name = 'cms/article-list.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ArticleNewView(TemplateView):
    template_name = 'cms/article-create.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [
        AllowAny
    ]