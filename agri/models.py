
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey, OneToOneField
from phonenumber_field.modelfields import PhoneNumberField

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
    Email = EmailField(unique=True,default=None)
   
    Address = models.CharField(max_length=100)
