from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email1 = models.EmailField()
    email2 = models.EmailField()
    mobile_number1 = models.CharField(max_length=255)
    mobile_number2 = models.CharField(max_length=255)
    age = models.IntegerField() 
    ig = models.CharField(max_length=255)
    x = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    snapchat = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    
   
