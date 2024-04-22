from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Attendance_mark(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_in = models.DateTimeField(default=timezone.now)
    time_out = models.DateTimeField(blank=True, null=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee_name} - Time In: {self.time_in}, Time Out: {self.time_out}"
