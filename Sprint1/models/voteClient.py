from django.db import models

from Sprint1.models import Article
from Sprint1.models import Client

class VoteClient(models.Model):
    """docstring for VoteClient"""
    #_idArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    #_idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    #_note = models.FloatField(null=False, blank=False)
    #_commentaire = models.TextField()
    #_dateVote = models.DateField(null=False, blank=False)

    #mutateurs et accesseurs
    def getDateVote(self):
        return self._dateVote

    def setDateVote(self, value):
        self._dateVote = value

    def getNote(self):
        return self._note

    def setNote(self, value):
        self._note = value

    def getCommentaire(self):
        return self._commentaire

    def setCommentaire  (self, value):
        self._commentaire = value
