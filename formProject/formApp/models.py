from django.db import models

class Practice(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    branch=models.CharField(max_length=30)
    college=models.CharField(max_length=30)

class Products(models.Model):
    pname=models.CharField(max_length=30)
    pno=models.IntegerField()
    pdetails=models.CharField(max_length=30)
    paddr=models.CharField(max_length=30)

# Create your models here.
