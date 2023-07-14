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
    
    # EmailField
    emp_email = forms.EmailField(
        label = "Employee Email",
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'example@example.com'
        }),
    )
    
    #ImageField
    emp_profile = forms.ImageField(
        label="Employee Profile Photo",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )
    
    # URLField
    emp_url = forms.URLField(
        label="Employee URL",
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Add your link'
            }
        )
    )