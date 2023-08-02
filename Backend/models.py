from django.db import models
from Userapp.models import Appointment

# Create your models here.

class Admin(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)

class Departmentdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Description = models.CharField(max_length=30, null=True, blank=True)

class Doctorsdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Department = models.CharField(max_length=30, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class AppointmentStatusHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('rejected', 'Rejected')])
    updated_by = models.ForeignKey(Admin, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

class TimeSlot(models.Model):
    Time = models.TimeField()
    Day = models.DateField()
    Doctor = models.CharField(max_length=20, null=True, blank=True)


