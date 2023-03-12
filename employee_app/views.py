from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User
from .models import (
    Department,
    Attendance,
    Employee_Applicant,
    Employee,
    Job_Application,
    )

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)

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


class EmployeeApplicantDetailView(DetailView):
    model = Employee_Applicant
    template_name = 'employee_app/eapplicatant_detail.html'

class ApplicantCreateView(LoginRequiredMixin, CreateView):
    model = Employee_Applicant
    template_name = 'employee_app/post_form.html'
    fields = ['job_application','employee_full_name','employee_bio', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ApplicantUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Employee_Applicant
    template_name = 'employee_app/post_form.html'
    fields = ['job_application','employee_full_name','employee_bio', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    

class ApplicantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee_Applicant
    success_url = '/'
    template_name = 'employee_app/post_form.html'

    def test_func(self):
        post = self.get_object()
        if self.request.employee == post.user:
            return True
        return False