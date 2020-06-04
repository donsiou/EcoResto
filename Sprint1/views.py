from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from Sprint1.models import Article, Ingredient, IngredientStock
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def Login(request):
    template = loader.get_template('Sprint1/login.html')
    return HttpResponse(template.render(request=request))


def Register(request):
    template = loader.get_template('Sprint1/register.html')
    return HttpResponse(template.render(request=request))


def index(request):
    template = loader.get_template('Sprint1/index.html')
    return HttpResponse(template.render(request=request))


def Ajouter_Article(request):
    if request.method == "POST":
        data = request.POST
        article = Article(_nom=data['article'], _type=data['type'], _quantite=data['quantite'], _prix=data['prix'],
                          _image=data['image'], _diponible=data['disponible'], _description=data['description'])
        article.ajouter()

        if article:
            print("ajoueté")
        else:
            print("delete")

    template = loader.get_template('Sprint1/GestionArticles_Ajouter.html')
    return HttpResponse(template.render(request=request))


def Articles(request):

    template = loader.get_template('Sprint1/GestionArticles_Afficher.html')
    return HttpResponse(template.render(request=request))


def Ingrediants(request):

    ingredient_list = Ingredient.objects.all()

    #template = loader.get_template('Sprint1/GestionIngredients_Afficher.html')
    # return HttpResponse(template.render(request=request))

    context = {
             'ingredient_list': ingredient_list
         }
    return render(request, 'Sprint1/GestionIngredients_Afficher.html', context)



def Ajouter_Ingrediant(request):
    if request.method == "POST":
        data = request.POST
        ingrediant = Ingredient(_nomIngred=data['Ingrediant'], _prixIngred=data['prix'],
                                _quantiteStock=data['quantite_stock'], _typeIngred=data['type'])
        ingrediant.ajouter()
        if ingrediant:
            print("ajoueté")
        else:
            print("delete")
    template = loader.get_template('Sprint1/GestionIngrediants_Ajouter.html')
    return HttpResponse(template.render(request=request))
