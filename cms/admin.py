from django.contrib import admin
from .models import Article, Image


# Register your models here.
class ImagesAdmin(admin.StackedInline):
    model = Article.images.though
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]


admin.site.register(Article, ArticleAdmin)
