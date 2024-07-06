from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from . import models

class RegistionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields = ('__all__')

