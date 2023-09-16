from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'emp_name',
        ]
    
    def clean_emp_name(self):
        emp_name = self.cleaned_data['emp_name']

        if emp_name == "":
            raise forms.ValidationError("The name filed cannot be empty")
        
        if emp_name == "Name" or "name":
            raise forms.ValidationError("Please Enter a valid name")
        
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