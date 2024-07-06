from django.urls import path
from .views import *
urlpatterns = [
    path('',movie_list,name='movies'),
    path('movies/<int:id>/',movie_detail,name='movie_detail'),
    path('registration/',registration,name="registration"),
    path('login/',loginpage,name='login'),
    path('logout/',logoutpage,name='logout')
]