from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_home),
    path('/add', views.add_book_page),
    path('/add_new_book', views.add_new_book),
    path('/book_detail/<int:book_id>', views.book_detail),
    path('/book_detail', views.book_detail),
]