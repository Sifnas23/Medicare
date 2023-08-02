from django.db import models

class Appointment(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Department = models.CharField(max_length=20, null=True, blank=True)
    Doctor = models.CharField(max_length=20, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
    PhoneNumber = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Place = models.CharField(max_length=20, null=True, blank=True)

class Signup(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)







