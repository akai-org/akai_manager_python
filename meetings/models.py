from django.db import models
from members.models import Member


class Meeting(models.Model):
    datetime = models.DateTimeField()
    agenda = models.TextField()
    notes = models.TextField()
    members = models.ManyToManyField(Member)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "Spotkanie " + str(self.datetime)
