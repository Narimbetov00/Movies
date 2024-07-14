from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.urls import reverse_lazy
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
            return   redirect('movies')
    else:
        form = RegistionForm()
    return render(request,'registration/registration.html',{'form':form})


def logoutpage(request):
    logout(request)
    return redirect('movies')


# KIRIW BOLIMI
# def loginpage(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request,data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect('homepage')
#     else:
#         form = AuthenticationForm()
#     return render(request,'login.html',{'form':form})




#Add comment 
# @login_required
def commmentView(request,id):
    user_id = request.user
    movie = get_object_or_404(Movies,id=id)
    if request.method == 'POST':
        text = request.POST['text']
        author = user_id
        obj = Comments(movie=movie,text=text,author=author)
        obj.save()
        return redirect('movies')
    return render(request,'comments.html',{'movie':movie})


def srcView(request):
    if request.method == 'GET':
        text = request.GET['src']
        print(text)
        
        obj= Movies.objects.all().values()
        movie_src = obj.get(name=text)
        movie_srclist = list(movie_src)
        context = {
            'movie_srclist':movie_srclist
        }
        # return HttpResponse('movies'+f"/{movie_src['id']}")
    return redirect('http://localhost:8000/movies/movies'+f"/{movie_src['id']}")
        # return render(request,'src.html',context)

