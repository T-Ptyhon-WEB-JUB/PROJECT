from django.db import models

# Create your models here.

class bus1(models.Model):
    name = models.CharField(max_length=30)
    phone= models.IntegerField(max_length=10)
    clas = models.CharField(max_length=5)
    address = models.CharField(max_length=30)

class bus2(models.Model):
        name = models.CharField(max_length=30)
        phone = models.IntegerField(max_length=10)
        clas = models.CharField(max_length=5)
        address = models.CharField(max_length=30)