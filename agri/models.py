
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey, OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from multiselectfield import MultiSelectField

#Create your models here.
class AgriUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = PhoneNumberField(default = None)
    is_farmer = models.BooleanField(default=False)
    is_Employee = models.BooleanField(default=False)
    is_private = models.BooleanField(default = False)
     

class FarmerUser(models.Model):   
    user = models.OneToOneField(AgriUser,on_delete=models.CASCADE,primary_key=True)
    adhaar = models.CharField(max_length=20,unique=True)
    village = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

class GovempUser(models.Model):
    user = models.OneToOneField(AgriUser,on_delete=models.CASCADE,primary_key=True)
    EmployeeId = models.CharField(max_length = 30,unique=True,default=None)  
    Address = models.CharField(max_length=100)

season_choice = (
    ('Rabi','Rabi'),
    ('Kharif','Kharif'),
    ('Zaid','Zaid'),
)

state_choice = (
    ('TS','Telangana'),
    ('AP','AndhraPradesh'),
    ('TN','Tamilnaidu'),
    ('KA','Karnataka'),
    ('MH','Maharastra'),
)

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = MultiSelectField(choices=season_choice,max_length=50)
    state = MultiSelectField(choices=state_choice,max_length=200)
    price = models.IntegerField()
    arrivals = models.DateTimeField(default=datetime.now,blank=True)
    pesticides = models.CharField(max_length=100)
    fertilizers = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    soil_health = models.CharField(max_length=100)
    crop_info = models.CharField(max_length = 2000)
    
    def __str__(self):
        return self.name

class Training(models.Model):
    crop = models.ForeignKey(Crop,on_delete=DO_NOTHING)
    vurl = models.CharField(max_length=150)
    desciption = models.CharField(max_length=1500)
    doc = models.FileField(default=None,upload_to = "/images")