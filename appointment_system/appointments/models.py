from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.name

def validate_evening_time(value):
    """
    Validates that the time is between 4 PM and 10 PM.
    """
    if not (value.hour >= 16 and value.hour <= 22):
        raise ValidationError("Time must be between 4 PM and 10 PM.")

class Availability(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    start_day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default='Monday')
    end_day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default='Friday')
    start_time = models.TimeField(validators=[validate_evening_time])
    end_time = models.TimeField(validators=[validate_evening_time])

    def clean(self):
        """
        Validates that the start day is before the end day.
        """
        if self.start_day_of_week > self.end_day_of_week:
            raise ValidationError("The start day of the week must be before the end day of the week.")

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_time = models.DateTimeField(default=timezone.now)


    # Add other fields as needed

