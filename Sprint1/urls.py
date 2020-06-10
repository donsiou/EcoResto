from django.conf.urls import url
from django.urls import path
from Sprint1 import views



urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('Ajouter_Article', views.Ajouter_Article),
    path('Articles', views.Articles),
    path('Ingrediants', views.Ingrediants),
    path('Ajouter_Ingrediant', views.Ajouter_Ingrediant),
    path('authentification', views.authentification),
    path('espace/<int:id>/', views.espace),
]