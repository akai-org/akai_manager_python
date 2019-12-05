from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    file = models.ImageField()
    name = models.TextField(null=False)
    url = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url}'

class Tag(models.Model):
    name = models.TextField(null=False)
    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    description = models.TextField(null=True)

    cover_image = models.TextField(null=False)
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

