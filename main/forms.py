from django import forms
from .models import Employee, position   # Import our Employee model here

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_name']
    
    def clean_emp_name(self):
        emp_name = self.cleaned_data['emp_name']
        if emp_name == "":
            raise forms.ValidationError("The name field cannot be empty")

        if emp_name == "Name":
            raise forms.ValidationError("Please enter a valid name")
        return emp_name

    emp_name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        initial="Name",
    )