from rest_framework import viewsets
from .serializers import ArticleSerializer, UpdateArticleListSerializer
from .models import Article


class ArticleListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = UpdateArticleListSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        id = self.kwargs['key']
        queryset = Article.objects.filter(id=id)
        return queryset
