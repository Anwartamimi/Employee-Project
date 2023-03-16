from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

from .forms import UserForm


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        response = redirect('/login/')
        return response
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

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(DepartmentList, self).get(request, **kwargs)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(DepartmentList, self).post(request, **kwargs)


class AttencanceListView(ListView):
    model = Attendance
    context_object_name = 'attendances'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(AttencanceListView, self).get(request, **kwargs)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(AttencanceListView, self).post(request, **kwargs)


class employee_applicantsList(ListView):
    model = Employee_Applicant
    context_object_name = 'employee_applicants'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(employee_applicantsList, self).get(request, **kwargs)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(employee_applicantsList, self).post(request, **kwargs)


class EmployeesListView(ListView):
    model = Employee
    context_object_name = 'employees'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(EmployeesListView, self).get(request, **kwargs)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(EmployeesListView, self).post(request, **kwargs)


class JobAapplicationsList(ListView):
    model = Job_Application
    context_object_name = 'job_applications'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(JobAapplicationsList, self).get(request, **kwargs)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            response = redirect('/login/')
            return response
        return super(JobAapplicationsList, self).post(request, **kwargs)


class EmployeeApplicantDetailView(DetailView):
    model = Employee_Applicant
    template_name = 'employee_app/eapplicatant_detail.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_app/employee_detail.html'


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

    def post(self, request, *args, **kwargs):
        if request.POST['status'] == 'Rejected' or request.POST['status'] == 'pending' :
            self.object = self.get_object()
            request.POST = request.POST.copy()
            request.POST['job_application'] = self.object.job_application
            request.POST['employee_full_name'] = self.object.employee_full_name
            request.POST['employee_bio'] = self.object.employee_bio

        else:

            self.object = self.get_object()
            request.POST = request.POST.copy()
           
            job_application = self.object.job_application
            full_name = self.object.employee_full_name
            bio = self.object.employee_bio

            job_application_id = request.POST['job_application']
            
            queryset = Job_Application.objects.filter(
                id=job_application_id).values('department')
                                    
            em = Employee.objects.create(
                full_name=full_name, 
                bio = bio,
                is_active = True,
                department_id = queryset,
                job_application_id = job_application_id,
                )
                    
        return super(ApplicantUpdateView, self).post(request, **kwargs)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_app/employee_detail.html'
    success_url = '/employees'
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        if request.POST['shift_ends_at'] == 'Null' or request.POST['shift_start_at'] == 'Null' :
            self.object = self.get_object()
            request.POST = request.POST.copy()
            
            request.POST['shift_ends_at'] = self.object.shift_ends_at
            request.POST['shift_start_at'] = self.object.shift_start_at

        else:

            self.object = self.get_object()
            request.POST = request.POST.copy()
           
            shift_start_at = self.object.shift_ends_at
            shift_ends_at = self.object.shift_start_at
            
             
        return super(EmployeeUpdateView, self).post(request, **kwargs)
    
    
    
class ApplicantDeleteView(DeleteView):
 
    model = Employee_Applicant
    success_url = '/employee_applicants'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_app/add_employee.html'
    fields = ['full_name','birth_date','department', 'bio', 'is_active', 'job_application', 'shift_start_at', 'shift_ends_at' ]

