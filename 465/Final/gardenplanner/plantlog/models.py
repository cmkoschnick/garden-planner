from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class PlantCategory(models.Model):
    season = models.CharField(max_length=128)
    def __str__(self):
        return self.season

class PlantEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(PlantCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    companions = models.CharField(max_length=200)
    incompatible = models.CharField(max_length=200)
    #incompatible =
