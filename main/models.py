from django.db import models

# Create your models here.
class position(models.Model):
    position_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.position_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
