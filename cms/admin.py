from django.contrib import admin
from .models import Article, Image, Tag


# Register your models here.
class ArticleImagesAdmin(admin.TabularInline):
    model = Article.images.through


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImagesAdmin]
    fields = ['title', 'description', 'cover_image', 'content', 'author', 'tags']


class ImagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImagesAdmin)
admin.site.register(Tag)
