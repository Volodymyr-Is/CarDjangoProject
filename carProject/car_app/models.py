from django.db import models



class Vehicle(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    image = models.URLField()
    price = models.IntegerField()
    distanceTraveled = models.IntegerField()
    maxSpeed = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.model} | ({self.type})'