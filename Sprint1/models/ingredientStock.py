from django.db import models


class IngredientStock(models.Model):
    _id_article = models.ForeignKey('self', on_delete=models.Article)
    _id_ingrediant = models.ForeignKey('self', on_delete=models.Ingredient)
    _quantite = models.FloatField()
    def __del__(self):
        print("del")

    def __init__(self, quantite):
        self._quantite = quantite
