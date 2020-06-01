from django.urls import path
from Sprint1 import views



urlpatterns = [
    path('', views.indexOuma),
    path('Ajouter_Article', views.Ajouter_Article),
    path('Articles', views.Articles),


]