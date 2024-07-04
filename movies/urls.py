from django.urls import path
from .views import *
urlpatterns = [
    path('',movie_list,name='movies')
]