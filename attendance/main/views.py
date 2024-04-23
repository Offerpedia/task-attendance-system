from datetime import datetime
import json
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeRegistrationForm
from django.http import JsonResponse
from .models import Attendance, Employee
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone
import logging

logger = logging.getLogger('mark.log')

@csrf_exempt


# Create your views here.

def login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('attendance')  # Redirect superuser to attendance.html
            elif hasattr(user, 'employee'):  # Check if user is linked to an employee
                return redirect('markattendance')  # Redirect employee to markattendance.html
            else:
                return redirect('some_other_view')  # Redirect for users who are neither
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')

def register(request):

    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assuming the form saves the user and creates an employee profile
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

@csrf_exempt  # Temporarily disable CSRF for this view, ideally use the CSRF token
def update_attendance(request):
    try:
        data = json.loads(request.body)  # Parse JSON data from the request body
        attendance_id = data.get('attendanceId')
        new_status = data.get('status')

        attendance = Attendance.objects.get(id=attendance_id)
        attendance.status = new_status
        attendance.approved = True if new_status == 'approved' else False
        attendance.save()

        return JsonResponse({'message': f'Attendance status updated to {new_status}.'})
    except Attendance.DoesNotExist:
        return JsonResponse({'error': 'Attendance record not found'}, status=404)
    except Exception as e:
        print("Exception", str(e))  # Printing the exception to the console for debugging
        return JsonResponse({'error': str(e)}, status=500)
def attendance(request):
    # Fetch all attendance records
    all_attendance_records = Attendance.objects.select_related('employee').order_by('-date')

    # Separate the records based on status
    approved_attendance = all_attendance_records.filter(status='approved')
    pending_attendance = all_attendance_records.filter(status='pending')
    print(approved_attendance)
    context = {
        'approved_attendance': approved_attendance,
        'pending_attendance': pending_attendance,
    }

    return render(request, 'main/attendance.html', context)

def markattendance(request):
    if request.method == 'POST':
        logger.info(f"Received POST data: {request.POST}")
        # Access the employee directly from the user. This assumes that the user model is linked to an employee model.
        user = request.user
        if hasattr(user, 'employee'):  # Check if the logged-in user has an associated employee
            employee = user.employee
            try:
                Attendance.objects.create(employee=employee, time_in=timezone.now())
                return JsonResponse({'message': 'Attendance marked successfully!'})
            except Exception as e:
                logger.error(f"Error marking attendance: {e}")
                return JsonResponse({'error': 'Failed to mark attendance'}, status=500)
        else:
            return JsonResponse({'error': 'No associated employee found'}, status=404)
    return render(request, 'main/markattendance.html')
