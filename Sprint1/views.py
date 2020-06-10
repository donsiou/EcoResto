from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from Sprint1.models import *

from Sprint1.forms import ConnexionForm


def Login(request):
    template = loader.get_template('Sprint1/login.html')
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


@login_required(login_url='/accounts/login/')
def Ajouter_Ingrediant(request):
    template = loader.get_template('Sprint1/GestionIngrediants_Ajouter.html')
    return HttpResponse(template.render(request=request))

def deconnexion(request):
    logout(request)

@login_required(login_url='Login')
def espace(request, id):
    type = "Vide"
    if id == 1:
        type = "Admin"
    if id == 2:
        type = "Client"
    if id == 3:
        type = "Accueil"
    if id == 4:
        type = "Desserte"
    return HttpResponse("Utilisateur = {} , Pseudo = {}".format(type, request.user.username))

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
            return HttpResponsePermanentRedirect('/espace/2')

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
