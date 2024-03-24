from django import forms
from django.db import models
from books_app.models import Book


class BookForms(forms.ModelForm):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    cover = models.ImageField(upload_to="books", default=None, null=True)

    class Meta:
        model = Book
        exclude = ['file']