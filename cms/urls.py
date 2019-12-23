from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/articles', views.ArticleViewSet)
router.register(r'api/tags', views.TagViewSet)

urlpatterns = [
    path('articles/', views.ArticleIndexView.as_view(), name="article_list"),
    path('articles/create', views.ArticleNewView.as_view(), name="article_create"),
] + router.urls
