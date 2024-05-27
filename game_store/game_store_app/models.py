from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

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
    description = models.CharField(max_length=1000)
    video_id = models.CharField(max_length=255)
    alt_title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="images", blank=True)
    genres = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def get_comments(self):
        return self.comments.all()


class CustomUser(AbstractUser):
    permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True
    )
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',
        blank=True
    )
    
# # class Comment(models.Model):
# #     games = models.ManyToManyField(Game, related_name='comments')
# #     users = models.ManyToManyField(CustomUser, related_name='user_comments')
# #     text = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    game = models.ForeignKey(Game, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)