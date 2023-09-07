from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    
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
    
    # ChoiceField
    emp_gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    # ManyToManyField
    emp_position = forms.ModelMultipleChoiceField(
        label = 'Employee Position',
        queryset = Position.objects.all(),
        widget = forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        })
    )
    
    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'emp_email',
            'emp_gender',
            'emp_position'
        ]