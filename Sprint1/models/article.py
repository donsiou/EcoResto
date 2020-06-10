from django.db import models

from Sprint1.models.ingredient import Ingredient
from Sprint1.models.menu import Menu


class Article(models.Model):
    """docstring for Accueil"""
    _nom = models.CharField(max_length=50, blank=False, null=False)
    _type = models.CharField(max_length=100, blank=False, null=False)
    _quantite = models.FloatField(null=False, blank=False)
    _image = models.ImageField()
    _prix = models.FloatField(null=False, blank=False)
    _description = models.TextField()
    _diponible = models.BooleanField(default=True)
    _ingrediants = models.ManyToManyField(Ingredient, through='IngredientStock')
    _menuAffecte = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    # _idMenu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # _ingredient = models.ManyToManyField(Ingredient, through='IngredientStock', related_name='+')
    # _quantiteIngred = models.ManyToManyField(Ingredient, related_name="_idArticle")

    def getAllIngredient(self):
        return self._ingrediants.all()

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
        i = Article.objects.filter(_nom__iexact=self._nom)
        return i.count() > 0

    def ajouterIngred(
            self):  # resette = IngredientStock(_idArticle=pasta,_idIngrediant=tonno,_quantite=1);resette.save()
        pass

    def supprimerIngred(self, nomIngrd):  # makedmatch mais b ORM ex ==> pasta._ingrediants.remove(tonno)
        ingrediant = Ingredient.objects.filter(_nomIngred=nomIngrd)
        if ingrediant.exist():
            self._ingrediants.remove(ingrediant)
            return True
        else:
            return False

    # mutateurs et accesseurs
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
        return self._diponible

    def setDisponible(self, value):
        self._diponible = value

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        self._description = value

    def getid(self):
        return self.id
    def getIngerds(self):
        return self._ingrediants