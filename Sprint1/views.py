from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.template import loader
from Sprint1.models import Utilisateur, Client


def index(request):
    return HttpResponse("Index de Sprint 1 modifié par RYM")


def indexPage(request):
    return HttpResponse("<h1>Hello world !</h1>")


def login(request):
    """Authenticate a user."""
    # Etape 1 :
    username = request.POST["username"]
    password = request.POST["password"]

    # Etape 2 :
    user = Utilisateur.authentification(request, username=username, password=password)

    # Etape 3 :
    if user is not None:
        Utilisateur.get_user(id)
        return HttpResponse("Vous etes connectée")
    else:
        return HttpResponse("Les champs renseignés sont invalides.")


