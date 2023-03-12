# Generated by Django 3.2 on 2023-03-12 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0004_employee_applicant_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_applicant',
            name='prefix',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(job_title__startswith='ahmad'), null=True, on_delete=django.db.models.deletion.PROTECT, to='employee_app.job_application'),
        ),
    ]