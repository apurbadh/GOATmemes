from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    birthdate = models.DateField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    pic = models.ImageField(upload_to="images/")


