from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    # CharField
    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        initial="Name",
    )
    # IntegerField
    emp_salary = forms.IntegerField(
        # min_value=0,
        # max_value=105,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        }),
        label="Employee Salary",
        initial=0,
    )
    # DateField
    employed_joining_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type':"date"
            }
        ),
        initial='2023-07-10'
    )