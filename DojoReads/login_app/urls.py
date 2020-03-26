from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_home),
    path('register', views.register),
    path('login', views.login),
    path('user', views.user_detail),
]