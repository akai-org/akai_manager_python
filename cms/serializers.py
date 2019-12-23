from rest_framework import serializers
from .models import Article, Tag
from django.contrib.auth.models import User
from html import unescape


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    cover_image = serializers.StringRelatedField()
    content = serializers.SerializerMethodField('get_content')

    class Meta:
        model = Article
        fields = ['title', 'content', 'description', 'cover_image', 'active', 'author', 'tags', 'images', 'created_at',
                  'updated_at']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

    def get_content(self, obj):
        if self.context.get('escape'):
            return obj.content
        else:
            return unescape(obj.content)


class UpdateArticleListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'updated_at']


class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    cover_image = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'cover_image', 'author', 'created_at', 'updated_at', 'active']
