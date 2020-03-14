from django.urls import path
from . import views

urlpatterns = [
    #books pages
    path('', views.books_page),
    path('add_book', views.add_book),
    path('book/<int:id>', views.book_info),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book),
    #author pages
    path('author_page', views.author_page),
    path('add_author', views.add_author),
    path('author/<int:id>', views.author_info),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),

]
