from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if "random_word" not in request.session:
        request.session['counter']=0
    return render(request, "show.html")

def random_word(request):
    request.session['counter']+=1
    request.session['random_word']=get_random_string(length = 14)

    return redirect('/')

def clear_screen(request):
    request.session.clear()
    return redirect('/')