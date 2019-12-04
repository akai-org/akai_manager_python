from django.urls import include, path
from . import views

urlpatterns = [
    path('api/articles/', views.ArticleListViewSet.as_view({'get': 'list'}), name="article_list"),
    path('api/articles/<int:key>/', views.ArticleViewSet.as_view({'get': 'list'}), name="article_list"),
]
