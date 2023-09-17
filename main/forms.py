from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    
    # CharField
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        initial="Name",
    )