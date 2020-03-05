# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("/placeholder to later display a list of all blogs")

# Create your views here.
def new(request):
    return HttpResponse("/placeholder to display a new form to create a new blog")

def create(request):
    redirect("/")

def show(request, blog_id):
    return HttpResponse(f"placeholder to display blog number:{blog_id}")

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {blog_id}")

def delete(request, blog_id):
    redirect("/")
