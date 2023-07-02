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
    # FloatField
    emp_score = forms.FloatField(
        min_value=0.0,
        max_value=10.0,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        }),
        label="Employee Salary",
        initial=0.0,
    )
    # BooleanField
    is_employed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label="Is Employed",
    )