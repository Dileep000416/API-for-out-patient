from datetime import timedelta
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Availability, Appointment
from .serializers import DoctorSerializer, AvailabilitySerializer, AppointmentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        # Custom logic before saving the appointment
        appointment_time = serializer.validated_data['appointment_time']
        doctor_id = serializer.validated_data['doctor'].id

        # Check if the appointment time is within the doctor's availability
        availability = Availability.objects.filter(
            doctor_id=doctor_id,
            start_time__lte=appointment_time.time(),
            end_time__gte=appointment_time.time()
        ).exists()

        if not availability:
            raise ValidationError("The appointment time is not within the doctor's availability.")

        # Check for overlapping appointments
        overlapping_appointments = Appointment.objects.filter(
            doctor_id=doctor_id,
            appointment_time__range=(appointment_time - timedelta(minutes=1), appointment_time + timedelta(minutes=1))
        ).exists()

        if overlapping_appointments:
            raise ValidationError("There is an overlapping appointment.")

        # Proceed with saving the appointment
        serializer.save()



class BulkDeleteDoctors(GenericAPIView):
    serializer_class = DoctorSerializer

    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        if ids:
            queryset = Doctor.objects.filter(id__in=ids)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No IDs provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)

# Add the doctor_detail view function here
from django.shortcuts import render, get_object_or_404
from .models import Doctor

from django.shortcuts import render, get_object_or_404
from .models import Doctor, Availability, Appointment

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    availabilities = Availability.objects.filter(doctor=doctor)
    appointments = Appointment.objects.filter(doctor=doctor)
    context = {
        'doctor': doctor,
        'availabilities': availabilities,
        'appointments': appointments,
    }
    return render(request, 'doctors.html', context)



