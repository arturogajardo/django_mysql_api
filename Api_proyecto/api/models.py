from django.db import models

# Create your models here.

class User(models.Model):
    usuario=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)