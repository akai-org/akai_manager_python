from django.db import models
from members.models import Member


class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    agenda = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(Member)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "Spotkanie " + str(self.date) + " o " + str(self.time)
