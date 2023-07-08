from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def home(request):
    return render(request, "main/home.html")

def employee_data(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['emp_name']

            emp_joining_date = form.cleaned_data['employed_joining_date']
            
            emp = Employee.objects.create(
                emp_name=name,
                employed_joining_date = emp_joining_date
            )
            
            emp.save()
            return HttpResponse("The data is saved in database")
    form = EmployeeForm()
    return render(request, 'main/employee.html', {'form': form})