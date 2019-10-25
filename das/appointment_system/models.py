from django.db import models

class Doctor_Details(models.Model):
    Doctor_ID       = models.AutoField(primary_key = True)
    Doctor_Name     = models.CharField(max_length  = 25)
    Specialization  = models.CharField(max_length  = 50)
    Address         = models.CharField(max_length  = 100)
    Email_ID        = models.EmailField(max_length = 40)
    Phone_Number    = models.CharField(max_length  = 25)
    
    def __str__(self):
         return self.Doctor_Name 

    class Meta:
        db_table             = 'doctors_details'
        verbose_name_plural  = "Doctor Details"

class Patient_Appointment(models.Model):
    Patient_ID       = models.AutoField(primary_key = True)
    Patient_Name     = models.CharField(max_length  = 25)
    Appointed_Doctor = models.ForeignKey(Doctor_Details, on_delete = models.CASCADE, null = True)
    Address          = models.CharField(max_length  = 100)
    Email_ID         = models.EmailField(max_length = 40)
    Phone_Number     = models.CharField(max_length  = 25)
    Time             = models.TimeField(auto_now=False, auto_now_add=False)
    Date             = models.DateField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Patient_Name
    
    class Meta:
        db_table             = 'patient_appointment'
        verbose_name_plural  = "Patient Appointment Details"


