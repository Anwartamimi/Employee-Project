from django import forms
from .models import Employee


class UserForm(forms.ModelForm):

    class Meta:

        model = Employee
        fields = ['shift_start_at','shift_ends_at' , 'full_name','birth_date', 'department', 'bio', 'job_application', 'is_active',  ]

        widgets = {
            'shift_start_at': forms.TextInput(attrs={'readonly':'readonly'}),
            'shift_ends_at': forms.TextInput(attrs={'readonly':'readonly'}),
        }

def clean_shift(self):
    return self.initial['shift_start_at', 'shift_ends_at']