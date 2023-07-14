from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_email = models.EmailField(null=True, blank=True)
    emp_profile = models.ImageField(null=True, blank=True, upload_to="emp_profile_pics/")
    emp_url = models.URLField(null=True, blank=True)