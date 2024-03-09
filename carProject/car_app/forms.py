from django import forms
from django.db import models
from car_app.models import *


class VehicleForms(forms.ModelForm):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    image = models.URLField()
    price = models.IntegerField()
    distanceTraveled = models.IntegerField()
    maxSpeed = models.IntegerField()

    class Meta:
        model = Vehicle
        exclude = ['file']