from django.db import models
from Doctors.models import Doctor

class Appointment(models.Model):
    appointment_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    doctor = models.CharField(max_length=100)
    mobile = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    description = models.TextField()


    def save(self, *args, **kwargs):
        if not self.appointment_number:
            last_appointment = Appointment.objects.order_by('-appointment_number').first()
            if last_appointment:
                self.appointment_number = last_appointment.appointment_number + 1
            else:
                self.appointment_number = 1
        super().save(*args, **kwargs)