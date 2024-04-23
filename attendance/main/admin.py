from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Attendance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department', 'phone')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'time_in', 'time_out', 'approved')
    actions = ['approve_attendance']

    def approve_attendance(self, request, queryset):
        queryset.update(approved=True)
    approve_attendance.short_description = "Mark selected attendance records as approved"

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
