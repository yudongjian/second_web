from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    photo_path = models.CharField(max_length=32)
    desc = models.CharField(max_length=32)


class User(models.Model):
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=12)