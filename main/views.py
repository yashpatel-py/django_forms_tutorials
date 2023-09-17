from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee


# Create your views here
def home(request):
    return render(request, "main/home.html")

def employee_data(request):    
    # def create_employee(request):
    if request.method == 'POST':
        # If the request method is POST, it means the form is submitted
        form = EmployeeForm(request.POST)

        if form.is_valid():
            # If the form is valid, save the data to the database
            form.save()
            # Redirect to a success page or another view
            return HttpResponse("The data is saved in database")
    else:
        # If the request method is GET, it means the user is accessing the form
        form = EmployeeForm()

    return render(request, 'main/employee.html', {'form': form})