from django.contrib import admin
from .models import Appointment
# Register your models here.



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name','doctor','date','time','appointment_number')