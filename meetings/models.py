from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    agenda = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User)
    is_active = models.BooleanField(default=False)
    code = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f'Spotkanie {str(self.date)} o {str(self.time)}'

    def save(self, *args, **kwargs):
        self.code = get_random_string(length=32)
        while Meeting.objects.filter(code=self.code):
            self.code = get_random_string(length=32)
        super().save(*args, **kwargs)


class Attendance(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.CASCADE)
    meeting = models.ForeignKey(Meeting, models.CASCADE)


