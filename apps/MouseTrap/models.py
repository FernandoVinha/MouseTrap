from django.db import models
from users.models import *
# Create your models here.

class Rats(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

# Update the model name from PictureSensor to MouseTrap
class MouseTrap(models.Model):
    image = models.ImageField(upload_to="apps/static/assets/img/temp") 
    rats = models.ForeignKey(Rats, on_delete=models.CASCADE, null=True,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_link(self):
        link = str(self.image).replace('MouseTrap','')
        return(link)


    def __str__(self):
        return str(self.id)

# Update the model name from PictureSensor to MouseTrap
class MouseTrap2(models.Model):
    image = models.ImageField(upload_to="apps/static/assets/img/temp") 
    #rats = models.ForeignKey(Rats, on_delete=models.CASCADE, null=True,blank=True)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_link(self):
        link = str(self.image).replace('MouseTrap','')
        return(link)


    def __str__(self):
        return str(self.id)

