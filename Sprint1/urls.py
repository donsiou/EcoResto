from django.urls import path
from Sprint1 import views



urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('Ajouter_Article', views.Ajouter_Article, name='Ajouter_Article'),
    path('Articles', views.Articles),
    path('Ingrediants', views.Ingrediants),
    path('Ajouter_Ingrediant', views.Ajouter_Ingrediant),



]