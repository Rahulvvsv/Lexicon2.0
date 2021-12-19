
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
    ('Telangana','Telangana'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Karnataka','Karnataka'),
    ('Maharastra','Maharastra'),
)

class Crop(models.Model):
    name = models.CharField(max_length=100)
    crop_info = models.TextField(max_length=3000)
    season = MultiSelectField(choices=season_choice,max_length=50)
    climate = models.TextField(max_length=2000)
    state = MultiSelectField(choices=state_choice,max_length=200,default="Telangana")
    price = models.IntegerField()
    photo = models.ImageField(blank=True,null=True,upload_to='images/')
    pesticides = models.CharField(max_length=100)
    fertilizers = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    soil_health = models.CharField(max_length=100)
    soil_info = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class Training(models.Model):
    crop = models.ForeignKey(Crop,on_delete=DO_NOTHING)
    vurl = models.CharField(max_length=150)
    desciption = models.CharField(max_length=1500)
    doc = models.FileField(default=None,upload_to = "images/")



class BlogContent11(models.Model):
        # id = models.BigIntegerField(primary_key = True)
        user  = models.ForeignKey(User,related_name='stories',on_delete=models.CASCADE)
        title = models.CharField(max_length = 50)
        story = models.CharField(max_length=5000)
        def __str__(self):
            return self.user.username


class PublishUser(models.Model):
    title = models.CharField(max_length = 50)
    story = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class CommentUser(models.Model):
    post = models.ForeignKey(PublishUser,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.post.title
