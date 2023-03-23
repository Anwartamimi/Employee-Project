from django import forms
from .models import Employee


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shift_start_at'].required = True
        self.fields['shift_ends_at'].required = True

    class Meta:

        model = Employee
        fields = ['shift_start_at','shift_ends_at' , 'full_name','birth_date', 'department', 'bio', 'job_application', 'is_active',  ]

               
