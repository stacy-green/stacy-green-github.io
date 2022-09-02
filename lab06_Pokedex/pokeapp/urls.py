from django.urls import path
from . import views

urlpatterns = [
    path("pokemon/", views.pokemon, name="pokemon"),
    path("", views.index, name="index"),   
]
