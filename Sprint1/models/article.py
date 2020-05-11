from django.db import models


class Article(models.Model):
    """docstring for Accueil"""

    def __del__(self):
        print("dest")# Ingredient.__del__(self)

    def __init__(self, nom, type,quantite,image,prix,description,diponible): #, nomIngred, prixIngred, quantiteIngred, quantiteStock, typeIngred
        self._nom = nom
        self._type = type
        self._quantite = quantite
        self._image = image
        self._prix = prix
        self._description = description
        self._diponible = diponible
        #self._ingred=Ingredient(nomIngred, prixIngred, quantiteIngred, quantiteStock, typeIngred)

    def ajouter(self):
        return True

    def modifier(self):
        return True

    def supprimer(self):
        return True

    def exist(self):
        return True

    def ajouterIngred(self, nomIngrd, quantite):
        pass

    def supprimerIngred(self, nomIngrd):
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

    def getImage(self):
        return self._image

    def setImage(self, value):
        self._image = value

    def getType(self):
        return self._type

    def setType(self, value):
        self._type = value

    def getDisponible(self):
        return self._disponible

    def setDisponible(self, value):
        self._disponible = value

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        self._description = value