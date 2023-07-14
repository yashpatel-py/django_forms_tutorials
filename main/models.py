from django.db import models

# Create your models here.
class Employee(models.Model):
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_email = models.EmailField(null=True, blank=True)
    emp_gender = models.CharField(choices=gender_choices, null=True, blank=True, max_length=50)