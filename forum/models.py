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
    number_of_memes = models.IntegerField(default=0)


class Memes(models.Model):
    posted_by = models.CharField(max_length=128)
    posted_by_email = models.CharField(max_length=124)
    caption = models.CharField(max_length=124)
    likes = models.IntegerField()
    usr_img = models.CharField(max_length=124, null=True)
    meme = models.ImageField(upload_to="memes/")



