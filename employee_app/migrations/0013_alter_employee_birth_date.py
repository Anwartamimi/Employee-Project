# Generated by Django 4.1.7 on 2023-03-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0012_remove_employee_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
