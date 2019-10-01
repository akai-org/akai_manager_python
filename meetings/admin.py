from django.contrib import admin
from .models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    exclude = ('members',)


admin.site.register(Meeting, MeetingAdmin)
