from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.name

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.IntegerField() # 1 for Monday, 2 for Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    # Add other fields as needed

