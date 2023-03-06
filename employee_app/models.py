from django.db import models


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
    full_name = models.TextField()
    birth_date = models.DateField()
    joining_date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT)
    bio = models.TextField()
    is_active = models.BooleanField()
    job_application = models.ForeignKey(
        Job_Application, on_delete=models.PROTECT)
    shift_start_at = models.DateField()
    shift_ends_at = models.DateField()

        

class Employee_Applicant(models.Model):
    pass


class Attendance(models.Model):
    pass


