from django.conf.urls import url
from django.urls import path
from Sprint1 import views



urlpatterns = [
    path('', views.Login),
    path('index', views.index),
    path('Ajouter_Article', views.Ajouter_Article, name='Ajouter_Article'),
    path('addIngredToArticle', views.addIngredToArticle, name='addIngredToArticle'),
    path('Articles', views.Articles),
    path('Ingrediants', views.Ingrediants),
    path('Ajouter_Ingrediant', views.Ajouter_Ingrediant),
    path('SupprimerArticle',views.SupprimerArticle),
    path('SupprimerIngerdient',views.SupprimerIngerdient),
    path('authentification', views.authentification),
    path('espace/<int:id>/', views.espace),

]
