from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=2500, null=True, blank=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    total_beds = models.SmallIntegerField()
    address = models.CharField(max_length=1500)
    pincode = models.CharField(max_length=6)
    phone_area_code = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    country_code = models.CharField(max_length=5, default="+91")
    
    def __str__(self):
        return str(self.name)



class Patient(models.Model):
    name = models.CharField(max_length=500)
    contact = models.CharField(max_length=10)
    country_code = models.CharField(max_length=5, default="+91")
    adhaar_number = models.CharField(max_length=12, null=True,blank=True)
    admitted_to = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    admission_timestamp = models.DateTimeField(auto_now=True)
    discharge_timestamp = models.DateTimeField(editable=False, null=True)
    discharged = models.BooleanField(default=False)
   
    def __str__(self):
        return str(self.name)
        

# Ambulance will have status as occupied

# Medical services -> Medical Shops, Test Centers, Clinics will have occupancy number 