from Sprint1.models.utilisateur import Utilisateur
from django.db import models


class Desserte(Utilisateur):
    """docstring for Desserte"""

    _tel = models.CharField(max_length=20)

    def __del__(self):
        Utilisateur.__del__(self)

    def __init__(self, login, password):
        Utilisateur.__init__(self, login, password)

    @staticmethod
    def authentification(self, login, password):
        Utilisateur.authentification(self, login, password)

    def inscription(self, userTab):
        if self.exist(userTab) != True:
            print("")  # requete SQL
        else:
            print("Vous etes deja presant dans BD")

    def exist(self):
        pass

    def supprimer(self):
        pass

    def modifier(self):
        pass

    def donnerNote(self, article, note):
        pass

    # mutateurs et accesseurs
