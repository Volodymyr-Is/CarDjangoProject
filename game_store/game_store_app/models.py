from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", default=None, null=True, blank=True)

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Developer(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="images", default=None, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.CharField(max_length=255)
    platform = models.ManyToManyField(Platform)
    description = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    alt_title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="images", blank=True)
    genres = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)