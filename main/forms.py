from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    # CharField
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
        }),
        initial="Name",
    )
    
    emp_email = forms.EmailField(
        label = "Employee Email",
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'example@example.com'
        }),
    )
    
    # DateTimeField
    employed_joining_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }
        ),
        initial='2023-07-10'
    )