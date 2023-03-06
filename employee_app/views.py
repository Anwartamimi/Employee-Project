from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User
from .models import (
    Department,
    Attendance,
    Employee_Applicant,
    Employee,
    Job_Application,
    )


from django.views.generic.list import ListView

# Create your views here.

def home(request):
    
    return render(request, 'employee_app/home.html', {})

def settings(request):
    
    return render(request, 'employee_app/settings.html', {})

def notifications(request):
    
    return render(request, 'employee_app/notifications.html', {})


class DepartmentList(ListView):
    model = Department
    context_object_name = 'departments'


class AttencanceListView(ListView):
    model = Attendance
    context_object_name = 'attendances'

class employee_applicantsList(ListView):
    model = Employee_Applicant
    context_object_name = 'employee_applicants'


class EmployeesListView(ListView):
    model = Employee
    context_object_name = 'employees'

        

class JobAapplicationsList(ListView):
    model = Job_Application
    context_object_name = 'job_applications'

