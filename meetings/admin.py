from django.contrib import admin
from .models import Meeting, Attendance


class MeetingAdmin(admin.ModelAdmin):
    exclude = ('members',)


class AttendanceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Attendance, AttendanceAdmin)
