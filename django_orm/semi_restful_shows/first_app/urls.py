from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='tvshow_home'),
    path('tvshow/tvshow_new/', views.tvshow_new),
    path('add_tvshow', views.add_tvshow),
    path('tvshow_info/<int:id>', views.tvshow_info),
    path('tvshow_info/<int:id>/edit/', views.edit_tvshow),
    path('delete_tvshow/<int:id>', views.delete_tvshow),
    path('change_tvshow/<int:id>', views.change_tvshow)
]
