from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateField(null=True)
    appointment_time = models.TimeField(null=True)
    approved = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)

    def __str__(self):
        return f'Appointment with {self.phone_number} on {self.appointment_date} at {self.appointment_time}'
