from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, User, Review
# Create your views here.


def valid_in_session(request):
    if not 'id' in request.session:
        print('not in session')
        return redirect('/')
    return True

def valid_post_in_session(request):
    if request.method!='POST':
        print('not a valid post')
        return False
    if not 'id' in request.session:
        print('not in session')
        return False
    return True

def book_home(request):
    if not valid_in_session:
        return redirect ('/')
    context={
        'user': User.objects.get(id=request.session['id']),
        'all_book':Book.objects.all(),
    }
    return render (request, 'book_home.html', context)


def add_book_page(request):
    if not valid_in_session:
        return redirect ('/')

    context={
        'all_author': Book.objects.all(),
    }
    return render(request, 'new_book.html', context)
    
def add_new_book(request):
    if not valid_post_in_session:
        return redirect ('/')
    errors=Book.objects.book_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/book/add')
    user = User.objects.get(id=request.session['id'])
    NewBook = Book.objects.create(user=user, title=request.POST['title'], author=request.POST['author'], rating=request.POST['rating'])
    NewReview = Review.objects.create(content=request.POST['content'])
    return redirect(f"/book/book_detail/{NewBook.id}")

def book_detail(request,book_id):
    if not valid_in_session:
        return redirect ('/')
    context={
        'all_user': User.objects.all(),
        'this_book': Book.objects.get(id=book_id),
        'all_review': Review.objects.all()
    }
    return render (request, 'book_details.html', context)