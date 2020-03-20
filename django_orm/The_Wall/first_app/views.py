from django.shortcuts import render, redirect
from .models import Post, User, Comment


# Create your views here.
def home(request):
    context={
        'all_post': Post.objects.all()
    }
    return render(request, 'index.html', context)

def login(request):
    return redirect('success/')

def success(request):
    context={
        "you have successfully logged into the wall"
    }
    return render(request, 'success.html', context )