from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.position_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.emp_name