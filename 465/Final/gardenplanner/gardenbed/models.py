from django.db import models
from django.contrib.auth.models import User

class BedCategory(models.Model):
    season = models.CharField(max_length=128)
    def __str__(self):
        return self.season

# Create your models here.
class BedEntry(models.Model):
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    season = models.ForeignKey(BedCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=4)
    value = models.CharField(max_length=100)
    idx = models.SmallIntegerField(default=100)
    class Meta:
	    unique_together = (("user", "location", "idx"))
