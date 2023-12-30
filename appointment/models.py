from django.db import models

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    
    