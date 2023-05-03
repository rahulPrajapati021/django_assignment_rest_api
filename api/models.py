from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Work(models.Model):
    artist_name = models.CharField(max_length=200)
    link = models.URLField()
    work_type = models.CharField(max_length=50)

# class Artist(models.Model):
#     name = models.CharField(max_length=200)
#     works = models.ManyToManyField('Work')

class Client(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)