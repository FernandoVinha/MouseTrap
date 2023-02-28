from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from datetime import date




class User(AbstractUser):
    profession = models.CharField(max_length=255,null = True,blank=True)
    avatar =  models.ImageField(upload_to= 'apps/static/assets/img/temp/',null = True,blank=True)
    background = models.ImageField(upload_to= 'apps/static/assets/img/temp/',null = True,blank=True)
    profile_information = models.TextField(null = True,blank=True)
    location = models.CharField(max_length=255,null = True,blank=True)
    mobile = models.CharField(max_length=255,null = True,blank=True)

    def avatar_link(self):
        link = str(self.avatar).replace('apps/','')
        return(link)

    def background_link(self):
        link = str(self.background).replace('apps/','')
        return(link)

class Company(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    def __str__(self):
        return str(self.name)
