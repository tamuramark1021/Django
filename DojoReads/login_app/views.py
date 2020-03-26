from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
# Create your views here.

def login_home(request):
    return render(request, 'login_home.html')

def register(request):
    errors=User.objects.register_validator(request.POST)
    if len(errors)>0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pwhash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash)
        request.session['id']=user.id
    return redirect('/book')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)    
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user= User.objects.get(email=request.POST['email'])
            request.session['id']=user.id 
    return redirect('/book')

def user_detail(request):
    context={
        
    }
    return render (request, 'user_detail.html', context)
