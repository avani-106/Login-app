from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)