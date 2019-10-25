from django.urls import include, path
from rest_framework import routers
from appointment_system.views import DoctorsList, AppointmentList

urlpatterns = [
    path('doctorDetails/', DoctorsList.as_view()),
    path('appointmentDetails/', AppointmentList.as_view())
]