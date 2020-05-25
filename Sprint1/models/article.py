from django.db import models


class Article(models.Model):
    """docstring for Accueil"""
    _idArticle = models.AutoField(primary_key=True)
    _nom = models.CharField(max_length=50, blank=False, null=False)
    _type = models.CharField(max_length=100,blank=False, null=False)
    _quantite = models.FloatField(null=False, blank=False)
    _image = models.ImageField()
    _prix = models.PositiveSmallIntegerField(null=False,blank=False)
    _description = models.TextField()
    _diponible = models.BooleanField(default=True)

    def __del__(self):
        print("destructeur article")

    def __init__(self, nom, type,quantite,prix,diponible,image="",description=""):
        self._nom = nom
        self._type = type
        self._quantite = quantite
        self._prix = prix
        self._diponible = diponible
        self._image = image
        self._description = description

    def getAllIngredient(self):
        pass

    def ajouter(self):
        return True

    def modifier(self):
        return True

    def supprimer(self):
        return True

    def exist(self):
        if (self._diponible):
            return True
        return False

    def ajouterIngred(self, nomIngrd, quantite):
        pass

    def supprimerIngred(self, nomIngrd):
        pass

    #mutateurs et accesseurs
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