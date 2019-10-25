from .models import Doctor_Details, Patient_Appointment
from rest_framework import serializers


class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Details
        fields = ['Doctor_Name', 'Specialization', 'Address', 'Email_ID', 'Phone_Number']


class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Appointment
        fields = ['Patient_Name', 'Appointed_Doctor', 'Address', 'Email_ID', 'Phone_Number', 'Time', 'Date']