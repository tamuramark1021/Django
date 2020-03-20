from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_user', views.add_user),
    path('login', views.login),
    path('success', views.success)
]