from django.db import models
from users.models import *
# Create your models here.

# Update the model name from PictureSensor to MouseTrap
class SMALLS(models.Model):
    _id = models.CharField(max_length=255,unique=True)
    Latitude = models.CharField(max_length=255,unique=True)
    Longitude = models.CharField(max_length=255,unique=True)
    GPSHora = models.CharField(max_length=255,unique=True)
    GPSMinuto = models.CharField(max_length=255,unique=True)
    GPSSegundo = models.CharField(max_length=255,unique=True)
    Acelerômetro1x = models.CharField(max_length=255,unique=True)
    Acelerômetro1y = models.CharField(max_length=255,unique=True)
    Acelerômetro1z = models.CharField(max_length=255,unique=True)
    Acelerômetro2x = models.CharField(max_length=255,unique=True)
    Acelerômetro2y = models.CharField(max_length=255,unique=True)
    Acelerômetro2z = models.CharField(max_length=255,unique=True)
    Umidade = models.CharField(max_length=255,unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
