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
    code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f'Spotkanie {str(self.date)} o godzinie {str(self.time)}'

    def save(self, *args, **kwargs):
        if self.is_active and not self.code:
            self.code = f"{random.randint(1, 999999):06d}"
            while Meeting.objects.filter(code=self.code):
                self.code = f"{random.randint(1, 999999):06d}"
        elif not self.is_active and self.code:
            self.code = None
        super().save(*args, **kwargs)





