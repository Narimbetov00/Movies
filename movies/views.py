from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login,logout
from .models import *
from .forms import *

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


def movie_detail(request,id):
    movie = get_object_or_404(Movies,id=id)
    return render(request,'movie_detail.html',{'movie':movie})

#DIZIMNEN OTIW
def registration(request):
    if request.method == 'POST':
        form = RegistionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return   redirect('homepage')
    else:
        form = RegistionForm()
    return render(request,'registration.html',{'form':form})

# KIRIW BOLIMI
def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logoutpage(request):
    logout(request)
    return redirect('homepage')