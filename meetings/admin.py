from django.contrib import admin
from .models import Meeting
from django.contrib.auth.models import User


class MeetingAdmin(admin.ModelAdmin):
    exclude = ('members',)


admin.site.register(Meeting, MeetingAdmin)
