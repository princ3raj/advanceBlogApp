from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

# Create your models here.



class User(AbstractUser):
     pass

class NinoRooms(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    pg_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number=models.IntegerField()
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=2000, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    ac_prices=models.IntegerField()
    non_ac_prices=models.IntegerField()
    pg_image=models.ImageField(null=True,blank=True)
    pg_image_two=models.ImageField(null=True,blank=True)
    pg_image_three=models.ImageField(null=True,blank=True)
  
  
    def __str__(self):
          return  self.pg_name


  
  
