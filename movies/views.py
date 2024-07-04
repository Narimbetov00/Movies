from django.shortcuts import render,get_object_or_404,redirect
from .models import *
# Create your views here.


def movie_list(request,category_slug=None):
    category= None
    categories = Category.objects.all()
    movies = Movies.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
    return render(request,'movie_list.html',{
                      'category':category,
                      'categories':categories,
                      'movies':movies
                      })
