from django.contrib import admin
from .models import Meeting, Attendance


class MeetingAdmin(admin.ModelAdmin):
    exclude = ('members',)


class AttendanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Attendance, AttendanceAdmin)
