from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import random

# Create your views here.
def index(request):
    if "gold_count" not in request.session:
        request.session['gold_count']=0
    return render(request, "index.html")

def farm_gold(request):
    request.session['gold_count']+=random.randrange(10,20)
    return redirect('/')

def cave_gold(request):
    request.session['gold_count']+=random.randrange(5,10)
    return redirect('/')

def house_gold(request):
    request.session['gold_count']+=random.randrange(2,5)
    return redirect('/')

def casino_gamble(request):
    request.session['gold_count']+=random.randrange(-50,50)
    return redirect('/')