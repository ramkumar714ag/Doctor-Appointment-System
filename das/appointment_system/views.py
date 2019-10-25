from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor_Details as doctor, Patient_Appointment as appointment
from .serializers import DoctorDetailsSerializer, PatientAppointmentSerializer


class DoctorsList(APIView):
    """
    List all doctors, or create a new doctors list.
    """

    def get(self, request, format=None):
        doctors_list = doctor.objects.all()
        serializer = DoctorDetailsSerializer(doctors_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentList(APIView):
    """
    List all appointments, or create a new appointments.
    """
    
    def get(self, request, format=None):
        appointment_list = appointment.objects.all()
        serializer = PatientAppointmentSerializer(appointment_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     