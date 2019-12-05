from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = serializers.StringRelatedField(many=True)
    gallery = serializers.StringRelatedField(many=True)
    cover_image = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['title', 'content', 'description', 'cover_image', 'author', 'tags', 'gallery', 'created_at', 'updated_at']


class UpdateArticleListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'updated_at']
