from django.contrib import admin
from .models import Meeting, Attendance


class MeetingAdmin(admin.ModelAdmin):
    exclude = ('members',)


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Attendance)