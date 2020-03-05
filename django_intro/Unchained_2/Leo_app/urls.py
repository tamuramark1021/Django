from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('/new', views.new),
    path('/create', views.create),
    path('/<int:blog_id>', views.show),
    path('/<int:blog_id>/edit', views.edit),
    path('/<int:blog_id>/delete', views.delete)
]
