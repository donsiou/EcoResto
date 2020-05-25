from django.db import models
from Sprint1.models.ingredient import Ingredient
from Sprint1.models.article import Article


class IngredientStock(models.Model):
    _idArticle = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    _idIngrediant = models.ForeignKey(Article, on_delete=models.CASCADE)
    _quantite = models.FloatField()
    def __del__(self):
        print("del")

    def __init__(self, quantite):
        self._quantite = quantite
