from Sprint1.models.utilisateur import Utilisateur
from django.db import models


class Client(Utilisateur):
    """docstring for Client"""
    _etablissement = models.CharField(max_length=20, null=False)

    def __del__(self):
        Utilisateur.__del__(self)

    def __init__(self, login, password, etablissement):
        Utilisateur.__init__(self)
        self._etablissement = etablissement

    @staticmethod
    def authentification(self, login, password):
        Utilisateur.authentification(self, login, password)

    def inscription(self, userTab):
        if (self.exist(userTab) != True):
            print("")  # requete SQL
        else:
            print("Vous etes deja presant dans BD")

    def exist(self):
        pass

    def supprimer(self):
        pass

    def modifier(self):
        pass

    def commenter(self):
        pass

    def noter(self):
        pass

    # mutateurs et accesseurs
    def getEtablissement(self):
        return self._etablissement

    def setEtablissement(self, value):
        self._etablissement = value
