from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employee/', views.employee_data, name="employee")
]
