from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.
def books_page(request):
    context={
        "all_the_books":Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.POST['title'] and request.POST['desc']:
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def book_info(request, id):
    some_book=Book.objects.get(id=id)
    # all_the_authors= some_book.authors.all()
    context={
        "some_book":Book.objects.get(id=id),
        "all_the_authors": Author.objects.exclude(books=some_book) 
    }
    return render(request,'book_info.html', context)

def author_info(request, id):
    some_author= Author.objects.get(id=id)
    context={
        'some_author': Author.objects.get(id=id),
        'all_the_books': Book.objects.exclude(authors=some_author),
    }
    return render(request, "author_info.html", context)

def add_author_to_book(request,book_id):
    some_author=Author.objects.get(id=request.POST['author_id'])
    some_book=Book.objects.get(id=book_id)
    some_author.books.add(some_book)
    return redirect(f"/book/{book_id}")

def add_book_to_author(request,author_id):
    some_book=Book.objects.get(id=request.POST['book_id'])
    some_author=Author.objects.get(id=author_id)
    some_book.authors.add(some_author)
    return redirect(f"/author/{author_id}")

def author_page(request):
    context={
        "all_the_authors":Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    if request.POST['first_name'] and request.POST['last_name'] and request.POST['notes']:
        Author.objects.create(first_name=request.POST['first_name'], last_name= request.POST['last_name'], notes= request.POST['notes'])
    # print(f"adding the author {author.first_name} {author.last_name}")
    return redirect('/author_page')



def delete_author(request):
    some_author= Author.objects.get(id=author.id)
    some_author.delete()


#  need to add the paths for both the urls, views, and rendering into the html, needing to update the hrefs in html