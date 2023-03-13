from django.shortcuts import render

from django.contrib.auth.models import User
from .models import (
    Department,
    Attendance,
    Employee_Applicant,
    Employee,
    Job_Application,
    )

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)

# Create your views here.

def home(request):

    employees_count = Employee.objects.all().count()
    employees_applicant_count = Employee_Applicant.objects.all().count()
    department_count = Department.objects.all().count()

    
    return render(request, 'employee_app/home.html',
                   {'employees_count': employees_count,
                    'employees_applicant_count': employees_applicant_count,
                    'department_count': department_count,
                                                      })

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


class EmployeeApplicantDetailView(DetailView):
    model = Employee_Applicant
    template_name = 'employee_app/eapplicatant_detail.html'

class ApplicantCreateView(LoginRequiredMixin, CreateView):
    model = Employee_Applicant
    template_name = 'employee_app/post_form.html'
    success_url = '/employee_applicants'
    fields = ['job_application','employee_full_name','employee_bio', 'status']

    
class ApplicantUpdateView(UpdateView):
    model = Employee_Applicant
    template_name = 'employee_app/update_applicant.html'
    success_url = '/employee_applicants'
    fields = ['job_application','employee_full_name','employee_bio', 'status']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class ApplicantDeleteView(DeleteView):
 
    model = Employee_Applicant
    success_url = '/employee_applicants'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_app/add_employee.html'
    fields = ['full_name','birth_date','department', 'bio', 'is_active', 'job_application', 'shift_start_at', 'shift_ends_at' ]

    