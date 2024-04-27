from rest_framework import serializers
from .models import Doctor, Availability, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__' 

class AvailabilitySerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = Availability
        fields = '__all__' 

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')
        doctor, created = Doctor.objects.get_or_create(**doctor_data)
        availability = Availability.objects.create(doctor=doctor, **validated_data)
        return availability

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__' 