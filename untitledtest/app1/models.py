from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=12)


class Food(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    photo_path = models.CharField(max_length=32)
    desc = models.CharField(max_length=32)