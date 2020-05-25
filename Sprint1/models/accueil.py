from Sprint1.models.utilisateur import Utilisateur
from django.db import models


class Accueil(Utilisateur):
    """docstring for Accueil"""

    _tel = models.CharField(max_length=20, null=True)

    def __del__(self):
        Utilisateur.__del__(self)

    def __init__(self, login, password):
        Utilisateur.__init__(self, login, password)

    @staticmethod
    def authentification(self, login, password):
        Utilisateur.authentification(self, login, password)

    def inscription(self, login, password, userTab):
        pass

    def exist(self):
        pass

    def supprimer(self):
        pass

    def modifier(self):
        pass

# mutateurs et accesseurs
