from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Doctor's Name")
    qualification = models.CharField(max_length=100, verbose_name="Qualification")
    specialist = models.CharField(max_length=100, verbose_name="Specialization")
    # Add other fields as needed

    def __str__(self):
        return self.name

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
    day_of_week = models.IntegerField(verbose_name="Day of Week") # 1 for Monday, 2 for Tuesday, etc.
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
    patient_name = models.CharField(max_length=100, verbose_name="Patient's Name")
    appointment_time = models.DateTimeField(verbose_name="Appointment Time")
    # Add other fields as needed
