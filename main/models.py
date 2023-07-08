from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    employed_joining_date = models.DateTimeField(null=True, blank=True)