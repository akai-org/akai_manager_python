from django.db import models
from django.contrib.auth.models import User
import random


class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    agenda = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User)
    is_active = models.BooleanField(default=False)
    code = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f'Spotkanie {str(self.date)} o {str(self.time)}'

    def save(self, *args, **kwargs):
        if self.is_active and not self.code:
            self.code = random.randint(1, 999999)
            while Meeting.objects.filter(code=self.code):
                self.code = random.randint(1, 999999)
        super().save(*args, **kwargs)


class Attendance(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.CASCADE)
    meeting = models.ForeignKey(Meeting, models.CASCADE)


