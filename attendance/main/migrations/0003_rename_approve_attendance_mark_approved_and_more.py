# Generated by Django 5.0.4 on 2024-04-22 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_employee_attendance_mark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance_mark',
            old_name='approve',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='attendance_mark',
            old_name='employee_name',
            new_name='employee',
        ),
    ]
