from django.db import models
from django.conf import settings


class Student(models.Model):
    name = models.CharField(max_length=120,null=True,blank=True)
    fathers_name = models.CharField(max_length=120,null=True,blank=True)
    dob = models.DateField(max_length=120,null=True,blank=True,)
    address = models.CharField(max_length=320,null=True,blank=True)
    city = models.CharField(max_length=120,null=True,blank=True)
    pin = models.CharField(max_length=120,null=True,blank=True)
    email = models.CharField(max_length=120,null=True,blank=True)
    mobile = models.CharField(max_length=120,null=True,blank=True)
    std = models.CharField(max_length=120,null=True,blank=True)
    marks = models.CharField(max_length=120,null=True,blank=True)
    time=models.DateTimeField(blank=True,null=True)
    def __str__(self):

        return self.name

class City(models.Model):
    city=models.CharField(max_length=100,null=True,blank=True)
    lat=models.CharField(max_length=30,null=True,blank=True)
    lon=models.CharField(max_length=30,null=True,blank=True)
    country=models.CharField(max_length=30,null=True,blank=True)
    state=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.city

class Grade(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name



class Pin(models.Model):
    pincode=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.pincode
