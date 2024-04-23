
from django.contrib import admin
from django.urls import path

from main.views import login, register,  attendance, markattendance,update_attendance

urlpatterns = [
    path("",login,name='login'),
    path('register/', register, name='register'),
    path('attendance/', attendance, name='attendance'),
    path('markattendance/', markattendance, name='markattendance'),
    path('admin/', admin.site.urls),
    path('update_attendance/', update_attendance, name='update_attendance'),

]
