from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from . import models



# forms filesinda tiykarinan ozlermiz forma jaratiw imkanin beredi

# class RegistionForm bul UserCreationForm dan miyras alip turipti 
class RegistionForm(UserCreationForm): # UserCreationForm path joli  from django.contrib.auth.forms import UserCreationForm
    class Meta:
        model = User    #  User  BiZ django makemigrations qilganimizda avto jaratiladi path joli from django.contrib.auth.models import User
        fields = ['email','username','password1','password2']   #Paydalaniwshi kiritiw kerek bolgan bolimler
    



# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username','password']


# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = models.Movies
#         fields = ('__all__')

