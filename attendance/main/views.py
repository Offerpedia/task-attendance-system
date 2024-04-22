from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeRegistrationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            if user.is_superuser:
                return redirect('attendance')  # Redirect superuser to attendance.html
            elif user.is_employee:
                return redirect('markattendance')  # Redirect employee to markattendance.html
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')  # Redirect to login page after successful registration
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def attendance(request):
    return render(request, 'main/attendance.html')

def markattendance(request):
    return render(request, 'main/markattendance.html')

