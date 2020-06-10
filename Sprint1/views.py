from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Sprint1.models import *
from Sprint1.forms import ConnexionForm


def menu(request):
    template = loader.get_template('Sprint1/Menu_.html')
    return HttpResponse(template.render(request=request))


def Login(request):
    template = loader.get_template('Sprint1/login.html')
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


def addIngredToArticle(request):
    ingredient_list = Ingredient.objects.all()
    article_list = Article.objects.all()
    if request.method == "POST":
        data = request.POST
        art = Article.objects.filter(id=data['article_list'])

        ingred = Article.objects.filter(id=data['ingredients'])
    if request.method == 'GET':
        add = request.GET
        ingredStock = IngredientStock(_idArticle=art, _idIngrediant=ingred, _quantite=data['quan'])

        ingredStock.save()

        if ingredStock:
            print("ajoueté")
        else:
            print("delete")
    context = {'ingredient_list': ingredient_list, 'article_list': article_list}
    return render(request, 'Sprint1/GestionIngrediants_Article.html', context)


def Articles(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list}
    #if request.method == "POST":
        #data = request.POST
        #art = Article.objects.filter(id=data['article_list'])
    return render(request, 'Sprint1/GestionArticles_Afficher.html', context)


def Ingrediants(request):
    ingredient_list = Ingredient.objects.all()
    context = {'ingredient_list': ingredient_list}
    return render(request, 'Sprint1/GestionIngredients_Afficher.html', context)


@login_required(login_url='/accounts/login/')
@csrf_exempt
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

def deconnexion(request):
    logout(request)

@login_required(login_url='Login')
def espace(request, id):
    nom = request.user.username
    type = "Vide"
    if id == 1:
        type = "Admin"
    if id == 2:
        type = "Client"
    if id == 3:
        type = "Accueil"
    if id == 4:
        type = "Desserte"
    context = {'nom': nom}
    return render(request, 'Sprint1/index.html', context)

def Register(request):
    template = loader.get_template('Sprint1/register.html')
    return HttpResponse(template.render(request=request))

def inscription(request):
    nom = request.POST['nom_ins']
    prenom = request.POST['prenom_ins']
    profession = request.POST['profession_ins']
    etablissement = request.POST['etablissement_ins']
    nationalite = request.POST['nationalite_ins']
    dateNaissance = request.POST['dateNaissance_ins']
    date = datetime.strptime(dateNaissance, '%Y-%m-%d')
    email = request.POST['email_ins']
    login = request.POST['login_ins']
    mdp = request.POST['mdp_ins']
    valide = Client.inscription(login, email, mdp,
                date, nationalite, profession, etablissement)
    if valide:
        return HttpResponsePermanentRedirect('Login')
    return HttpResponseRedirect('inscription')

def SupprimerIngerdient(request):
    if request.method == 'GET':
        data = request.GET
        ingrediant = Ingredient.objects.get(id=data['id'])
        ingrediant.supprimer()
    template = loader.get_template('Sprint1/GestionIngrediants_supprimer.html')
    return HttpResponse(template.render(request=request))

def SupprimerArticle(request):
    if request.method == 'GET':
        data = request.GET
        article = Article.objects.get(id=data['id'])
        article.supprimer()
    template = loader.get_template('Sprint1/GestionArticles_supprimer.html')
    return HttpResponse(template.render(request=request))

@csrf_exempt
def authentification(request):
    from django.contrib.auth import login
    form = ConnexionForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["login"]
        password = form.cleaned_data["mdp"]

        if Admin.authentification(username, password):
            utilisateur = Admin.authentification(username, password)
            login(request, utilisateur.user)
            return HttpResponsePermanentRedirect('/espace/1')

        elif Client.authentification(username, password):
            utilisateur = Client.authentification(username, password)
            login(request, utilisateur.user)
            context = {'nom': utilisateur.user.username}
            return render(request, 'Sprint1/index.html', context)

        elif Accueil.authentification(username, password):
            utilisateur = Accueil.authentification(username, password)
            login(request, utilisateur.user)
            return HttpResponsePermanentRedirect('/espace/3')

        elif Desserte.authentification(username, password):
            utilisateur = Desserte.authentification(username, password)
            login(request, utilisateur.user)
            return HttpResponsePermanentRedirect('/espace/4')

    #Pour afficher un message d'erreur dans la page de connexion
    return HttpResponseRedirect('/Login', {'erreur' : True})
