from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from game_store_app.models import Comment, CustomUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser