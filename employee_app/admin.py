from django.contrib import admin
from .models import (
    Department,
    Job_Application,
    Employee,
    Employee_Applicant,
    Attendance)


class DepartmentAdmin(admin.ModelAdmin):
    list_display =['name',]
    fields = ['name',]


class Job_ApplicationAdmin(admin.ModelAdmin):
    list_display =['job_title', 'job_description', 'is_published', 'department']
    fields =['job_title', 'job_description', 'is_published', 'department']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'department',
                    'is_active', 'job_application',
                    'shift_start_at', 'shift_ends_at']
    

class EmployeeApplicantAdmin(admin.ModelAdmin):
    list_display =['job_application', 'employee_full_name', 'employee_bio', 'status']


admin.site.register(Employee_Applicant, EmployeeApplicantAdmin)
admin.site.register(Attendance)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Job_Application, Job_ApplicationAdmin)
admin.site.register(Employee, EmployeeAdmin)