from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('attendances/', views.AttencanceListView.as_view(), name='attendances'),
    path('employee_applicants/', views.employee_applicantsList.as_view(), name='employee_applicants'),
    path('employees/', views.EmployeesListView.as_view(), name='employees'),
    path('job_applications/', views.JobAapplicationsList.as_view(), name='job_applications'),
    path('settings/', views.settings, name='settings'),
    path('notifications/', views.notifications, name='notifications'),
    path('departments/', views.DepartmentList.as_view(),name='departments'),
]
