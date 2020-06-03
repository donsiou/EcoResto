from django.db import models


class Ingredient(models.Model):
    _nomIngred = models.CharField(max_length=100, null=False, unique=True)
    _prixIngred = models.FloatField()
    _quantiteStock = models.FloatField()
    _typeIngred = models.CharField(max_length=100, null=False)

    # On a supprimer les  constrcuteurs et les destructeurs pour éviter les problémes
    # Le constructeur pour creer un objet ingredient, il faut indiquer les attributs
    ## i = Ingredient(_nomIngred="riz", _prixIngred=1000.0, _quantiteStock=1000.5, _typeIngred="Legume")
    def __str__(self):
        return self._nomIngred

    @staticmethod
    def getByName(nomIngred):
        i = Ingredient.objects.filter(_nomIngred__iexact=nomIngred)
        if i.count() == 0: return None
        return i[0]


    # False : L'ingredient existe déja
    # True : L'ingredient ajouté avec succé
    def ajouter(self):
        print("Hello world !")
        if self.exist():
            return False
        self.save()
        return True

    def modifier(self):
        if not self.exist():
            return False
        self.save()
        return True

    def supprimer(self):
        if not self.exist():
            return False
        self.delete()
        return True

    def exist(self):
        i = Ingredient.objects.filter(_nomIngred__iexact=self._nomIngred)
        return i.count() > 0

    def epuise(self, quantite=0.0):
        return (self._quantiteStock - quantite) <= 0

    def ajouterStock(self, quantite):
        if not self.exist():
            return False
        self.setQuantiteStock(self._quantiteStock - quantite)
        return True

    #-1 : L'ingredient n'existe pas
    #-2 : La quantite en stock n'est pas suffisante
    #0 : operation faite avec succe
    def soustraireStock(self, quantite):
        if not self.exist():
            return -1
        if self.epuise():
            return -2
        self.setQuantiteStock(self._quantiteStock - quantite)
        return 0

    def getNom(self):
        return self._nom

    def setNom(self, nom):
        self._nom = nom

    def getPrix(self):
        return self._prix

    def setPrix(self, value):
        self._prix = value

    def getQuantiteStock(self):
        return self._quantiteStock

    def setQuantiteStock(self, value):
        self._quantiteStock = value

    def getType(self):
        return self._type

    def setType(self, value):
        self._type = value
