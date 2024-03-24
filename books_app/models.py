from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="books", default=None, null=True)
    date = models.DateField(auto_now=False)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} ({self.author})'