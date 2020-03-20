from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt
# from .models import User, Registration, Login
# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_user(request):
    # errors={}
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        print("Errors", errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pwhash=bcrypt.hashpw(request.POST['password_register'].encode(), bcrypt.gensalt())
        user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email_register'], password=pwhash.decode())
        # request.session['id']= user.id
    return redirect('/success')
    
    
def login(request):
    # if request.method!='POST':
    #     return redirect('/')
    errors = User.objects.login_validator(request.POST)    
    if len(errors)>0:
        print("I'm in motha FFFF")
        for key, value in errors.items():
            messages.error(request, value)
            print("I am STUCK!!!!!!!!!!!!!!")
        return redirect('/')
    else:
        print("I'm in the ELSE")
        user= User.objects.get(email=request.POST['email_login'])
        request.session['id']=user.id 
    return redirect('/success')

def success(request):
    context = {
        'user':User.objects.get(id=request.session['id'])
    }
    return render(request, 'login.html', context)

# Create your views here.
