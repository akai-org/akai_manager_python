from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to="images/")
    name = models.CharField(null=False, max_length=256)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file}'

    def get_absolute_url(self):
        return "image", [self.slug]



class Tag(models.Model):
    name = models.CharField(null=False, max_length=256)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.CharField(null=False, max_length=256)
    content = models.TextField(null=False)
    description = models.TextField(null=True)

    cover_image = models.OneToOneField(Image, related_name="cover_image", on_delete=models.CASCADE, null=True)
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    images = models.ManyToManyField(Image, related_name="gallery", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
