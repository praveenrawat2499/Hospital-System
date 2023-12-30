from django.contrib import admin
from appointment.models import Appointment
# Register your models here.
class Appointment_admin(admin.ModelAdmin):
    list_display = ("name", "phone_no", "email", "hospital" , "department" , "doctor", "description", "date", "time")

admin.site.register(Appointment, Appointment_admin)


