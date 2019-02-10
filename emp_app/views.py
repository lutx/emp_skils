from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee

def index(request):

    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'index.html', context)

def employee(request):
    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'employee.html', context)