from django.urls import path, include
from . import views



urlpatterns = [
    path('', include(views.index)),
    path('/farm_gold', include(views.farm_gold)),
    path('/cave_gold', include(views.cave_gold)),
    path('/house_gold', include(views.house_gold)),
    path('/casino_gamble', include(views.casino_gamble)),
]
