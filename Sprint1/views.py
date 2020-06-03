from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


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
    template = loader.get_template('Sprint1/GestionArticles_Ajouter.html')
    return HttpResponse(template.render(request=request))


def Articles(request):
    template = loader.get_template('Sprint1/GestionArticles_Afficher.html')
    return HttpResponse(template.render(request=request))



def Ingrediants(request):
    template = loader.get_template('Sprint1/GestionIngredients_Afficher.html')
    return HttpResponse(template.render(request=request))

def Ajouter_Ingrediant(request):
    template = loader.get_template('Sprint1/GestionIngrediants_Ajouter.html')
    return HttpResponse(template.render(request=request))







