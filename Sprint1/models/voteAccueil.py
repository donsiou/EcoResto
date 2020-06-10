from django.db import models

from Sprint1.models import Article, Accueil


class VoteAccueil(models.Model):
    """docstring for VoteAccueil"""
    #_idArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    #_idAccueil = models.ForeignKey(Accueil, on_delete=models.CASCADE)
    #_quantiteAvant = models.FloatField(null=False, blank=False)
    #_quantiteApres = models.FloatField(null=False, blank=False)
    #_epuise = models.BooleanField(default=True)
    #_dateVote = models.DateField(null=False, blank=False)

    #mutateurs et accesseurs
    def getDateVote(self):
        return self._dateVote

    def setDateVote(self, value):
        self._dateVote = value

    def getQuantiteAvant(self):
        return self._quantiteAvant

    def setQuantiteAvant(self, value):
        self._quantiteAvant = value

    def getQuantiteApres(self):
        return self._quantiteApres

    def setQuantiteApres(self, value):
        self._quantiteApres = value

    def getEpuise(self):
        return self._epuise

    def setEpuise(self,value):
        self._epuise = value

