from django.db import models


class Member(models.Model):
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.email
