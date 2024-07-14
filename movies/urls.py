from django.urls import path
from django.urls import reverse_lazy
from .views import *
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',movie_list,name='movies'),
    path('src/',srcView,name='moviesrc'),
    path('movies/<int:id>/',movie_detail,name='movie_detail'),
    path('registration/',registration,name="registration"),
    #from django.contrib.auth.views import LoginView usidan paydalanildi
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logoutpage,name='logout'),
    path('<int:id>/comment/',commmentView,name='comments'),
]