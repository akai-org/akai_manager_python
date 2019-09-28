from django.db import models
from meetings.models import Meeting


class Member(models.Model):
    email = models.CharField(max_length=120)
    meetings = models.ManyToManyField(Meeting)

    def __str__(self):
        return self.email
