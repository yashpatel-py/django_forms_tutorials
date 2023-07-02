from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_salary = models.IntegerField(null=False, blank=False)
    emp_score = models.FloatField(null=True, blank=True)