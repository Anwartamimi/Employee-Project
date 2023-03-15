from django.urls import path
from . import views 
from .views import (
    ApplicantCreateView,
    EmployeeApplicantDetailView,
    ApplicantUpdateView,
    ApplicantDeleteView, 
    EmployeeCreateView,
    EmployeeUpdateView
    
    )


urlpatterns = [
    path('', views.home, name='home'),
    path('attendances/', views.AttencanceListView.as_view(), name='attendances'),
    path('employee_applicants/', views.employee_applicantsList.as_view(), name='employee_applicants'),
    path('employees/', views.EmployeesListView.as_view(), name='employees'),
    path('job_applications/', views.JobAapplicationsList.as_view(), name='job_applications'),
    path('settings/', views.settings, name='settings'),
    path('notifications/', views.notifications, name='notifications'),
    path('departments/', views.DepartmentList.as_view(),name='departments'),

    path('employee_applicants/new/', ApplicantCreateView.as_view(), name='applicant-create'),
    path('employee_applicants/<int:pk>', ApplicantUpdateView.as_view(), name='employee-applicant-update'),
    path('employee_applicants/<int:pk>/delete', ApplicantDeleteView.as_view(), name='employee-applicant-delete'),
    path('employees/new/', EmployeeCreateView.as_view(), name='new-employee'),

    path('employee/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-detail'),

]
