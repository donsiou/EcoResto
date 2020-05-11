from django.db import models


class Ingredient(models.Model):

    def __del__(self):
        print("del")

    def __init__(self, nomIngred, prixIngred, quantiteIngred, quantiteStock, typeIngred):
        self._nomIngred = nomIngred
        self._prixIngred = prixIngred
        self._quantiteIngred = quantiteIngred
        self._quantiteStock = quantiteStock
        self._typeIngred = typeIngred

    def ajouter(self):
        return True

    def modifier(self):
        return True

    def supprimer(self):
        return True

    def exist(self):
        return True

    def epuise(self):
        return True

    def ajouterStock(self, quantite):
        pass

    def soustraireStock(self, quantite):
        pass

    def getNom(self):
        return self._nom

    def setNom(self, nom):
        self._nom = nom

    def getPrix(self):
        return self._prix

    def setPrix(self, value):
        self._prix = value

    def getQuantite(self):
        return self._quantite

    def setQuantite(self, value):
        self._quantite = value

    def getQuantiteStock(self):
        return self._quantiteStock

    def setQuantiteStock(self, value):
        self._quantiteStock = value

    def getType(self):
        return self._type

    def setType(self, value):
        self._type = value
