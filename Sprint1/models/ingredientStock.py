from django.db import models


class IngredientStock(models.Model):

    def __del__(self):
        print("del")

    def __init__(self, quantite):
        self._quantite = quantite
