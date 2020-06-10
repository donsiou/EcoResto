from django.db import models
from Sprint1.models.ingredient import Ingredient
from Sprint1.models.article import Article


class IngredientStock(models.Model):
    _idArticle = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    _idIngrediant = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    _quantite = models.FloatField(null=True) # quantite ingrediant dans l'article

