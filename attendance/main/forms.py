from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from django.contrib.auth import get_user_model

class EmployeeRegistrationForm(UserCreationForm):
    employee_name = forms.CharField(max_length=100)
    employee_id = forms.CharField(max_length=20, required=True)
    department = forms.CharField(max_length=20, required=True)
    phone = forms.CharField(max_length=20, required=True)
    is_employee = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'employee_name', 'employee_id', 'department', 'phone', 'is_employee']
