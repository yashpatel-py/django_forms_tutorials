from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    emp_email = models.EmailField(null=True, blank=True)
    emp_files = models.FileField(null=True, blank=True, upload_to='file_uploads/')
    employed_joining_date = models.DateTimeField(null=True, blank=True)