from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    watering_schedule = models.IntegerField()

    def __str__(self):
        return self.name