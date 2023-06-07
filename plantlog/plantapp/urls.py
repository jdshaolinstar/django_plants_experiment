from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('add/', views.add_plant, name='add_plant'),
]