from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.position_name

class Employee(models.Model):
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_email = models.EmailField(null=True, blank=True)
    emp_gender = models.CharField(choices=gender_choices, null=True, blank=True, max_length=50)
    emp_position = models.ManyToManyField(Position, blank=True, null=True)
    
    def __str__(self):
        return self.emp_name