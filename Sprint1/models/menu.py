from django.db import models


class Menu(models.Model):
    """docstring for Menu"""
    _date = models.DateField(null=False, blank=False)
    _nomMenu = models.CharField(max_length=50)




    def supprimer(self,menu):
        if not self.exist():
            return False
        self.delete()
        return True

    def exist(self):
        i = Menu.objects.filter(_idMenu__iexact=self._idMenu)
        return i.count() > 0

    def ajouter(self):
        if self.exist():
            return False
        self.save()
        return True

    def modifierQuantite(self,article,quantite):
        pass

    def signalerArticleEpuisee(self,article):
        pass

    def getDesserts(self):
        pass

    def getPlatPrincipal(self):
        pass

    def getEntree(self):
        pass

    #mutateurs et accesseurs
    def getDate(self):
        return self._date

    def setDate(self, value):
        self._date = value