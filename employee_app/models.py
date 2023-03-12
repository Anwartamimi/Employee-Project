from django.db import models
from django.db.models import Q
from django.urls import reverse


class Department(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Job_Application(models.Model):
    job_title = models.TextField()
    job_description = models.TextField()
    is_published = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.job_title


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    joining_date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT)
    bio = models.CharField(max_length=500)
    is_active = models.BooleanField()
    job_application = models.ForeignKey(
        Job_Application, on_delete=models.PROTECT)
    shift_start_at = models.DateField(null=True, blank=True)
    shift_ends_at = models.DateField(null=True, blank=True)


class Employee_Applicant(models.Model):

    job_application = models.ForeignKey('Job_application', blank=True, null=True,
                               on_delete=models.PROTECT,
                               limit_choices_to=Q(is_published='True'))

    employee_full_name = models.CharField(max_length=100)
    employee_bio = models.CharField(max_length=500)

    status_choices = (
        ('Approved', ('Approved')),
        ('Rejected', ('Rejected')),
        ('pending', ('pending')),
    )

    status = models.CharField(choices=status_choices, max_length=15, default='pending')

    def get_absolute_url(self):
        return reverse("employee-applicant-detail", kwargs={"pk": self.pk})
    

class Attendance(models.Model):
    pass


