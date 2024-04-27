from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Availability, Appointment
from .serializers import DoctorSerializer, AvailabilitySerializer, AppointmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Add the doctor_detail view function here
from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctors.html', {'doctor': doctor})


