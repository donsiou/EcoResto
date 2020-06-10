from django.db import models

from Sprint1.models import Article, Desserte


class VoteDesserte(models.Model):
    """docstring for VoteDesserte"""
    #_idArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    #_idDessert = models.ForeignKey(Desserte, on_delete=models.CASCADE)
    #_note = models.FloatField(null=False, blank=False)
    #_dateVote = models.DateField(null=False, blank=False)

    def __del__(self):
        print("destructeur VoteDesserte")

    def __init__(self,note,dateVote):
        self._note = note
        self._dateVote = dateVote

    #mutateurs et accesseurs
    def getDateVote(self):
        return self._dateVote

    def setDateVote(self, value):
        self._dateVote = value

    def getNote(self):
        return self._note

    def setNote(self, value):
        self._note = value

