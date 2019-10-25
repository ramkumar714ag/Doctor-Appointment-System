from django.contrib import admin

# Register your models here.

from .models import Doctor_Details, Patient_Appointment

class doctorDetails(admin.ModelAdmin):
    list_display = ('Doctor_Name', 'Specialization', 'Address', 'Email_ID', 'Phone_Number')
    list_filter  = ('Doctor_Name',)
 
admin.site.register(Doctor_Details, doctorDetails)


class appointmentDetails(admin.ModelAdmin):
    list_display = ('Patient_Name', 'Appointed_Doctor', 'Address', 'Email_ID', 'Phone_Number', 'Time', 'Date')
    list_filter  = ('Patient_Name','Appointed_Doctor', 'Date')
  
admin.site.register(Patient_Appointment, appointmentDetails)
