from django.shortcuts import render
# from .models import User, Registration, Login
# Create your views here.

def home(request):
    return render(request, 'home.html')
