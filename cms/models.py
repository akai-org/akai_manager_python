from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    file = models.ImageField()
    name = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.TextField(null=False)

class Article(models.Model):
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    description = models.TextField(null=True)

    cover_image = models.OneToOneField(Image, on_delete=models.CASCADE())
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING())

    images = models.ManyToManyField(Image, on_delete=models.DO_NOTHING())
    tags = models.ManyToManyField(Tag, on_delete=models.DO_NOTHING())

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

