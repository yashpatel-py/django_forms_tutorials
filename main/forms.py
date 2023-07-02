from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        initial="Name",
        help_text="Please enter your full name (First Name Last name)"
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    emp_salary = forms.IntegerField()