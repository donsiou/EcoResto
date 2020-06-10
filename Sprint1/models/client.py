from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from Sprint1.models.utilisateur import Utilisateur
from django.db import models


class Client(Utilisateur):
    """docstring for Client"""
    etablissement = models.CharField(max_length=20, null=False)


    @staticmethod
    def authentification(login, password):
        from Sprint1.models import Admin, client, desserte, accueil
        user = authenticate(username=login, password=password)
        if user:
            id = user.id
            u = Client.objects.filter(user_id=id)
            if u.count() > 0:
                return u[0]
        return None

    @staticmethod
    def inscription(username, email, password, dateNaissance=None, nationalite="", profession="", etablissement=""):
        if Utilisateur.exist(username):
            return False

        user = User.objects.create_user(username, email, password)

        u = Client(user=user, dateNaissance=dateNaissance, nationalite=nationalite, profession=profession, etablissement=etablissement)
        user.save()
        u.save()
        return True

    def commenter(self):
        pass

    def noter(self):
        pass

    # mutateurs et accesseurs
    def getEtablissement(self):
        return self.etablissement

    def setEtablissement(self, value):
        self.etablissement = value
