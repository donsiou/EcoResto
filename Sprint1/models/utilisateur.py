from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone




class Utilisateur(models.Model):
    #Ici on a utilisé une liaison avec la classe User définit par défaut en django, afin de pouvoir géréer
    # les utilisateurs et les sessions facillement
    # La classe User conient déja les attributs de base pour un utilisateur :
        # username, password, email, first_name, last_name, date_joined
    # Donc inutile de les redéfinir  une autre fois dans notre classe !

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dateNaissance = models.DateField(null=True)
    nationalite = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    #Pour les contructeurs et les destructeurs django par défaut les crée pour nous, et qu'on a essayé de les redéfinir
    # cela nous causé beaucoup de problémes

    # On était obligé de mettre exist comme une méthode exist comme static à fin de pouvoir l'appelé dans les méthode
    # autentification et inscription qui sont statiques
    @staticmethod
    def exist(username):
        i = User.objects.filter(username__iexact=username)
        return i.count() > 0

    def supprimer(self, tabUser):
        if not Utilisateur.exist(self.user.username):
            return False
        self.save()
        return True

    def modifier(self):
        if not Utilisateur.exist(self.user.username):
            return False
        self.delete()
        return True

    # mutateurs et accesseurs
    def getPassword(self):
        return self._password

    def getLogin(self):
        return self._login

    def getNom(self):
        return self._nom

    def getPrenom(self):
        return self._prenom

    def getNationalite(self):
        return self._nationalite

    def getEmail(self):
        return self._email

    def getTel(self):
        return self._tel

    def getProfession(self):
        return self._profession

    def setProfession(self, value):
        self._profession = value

    def setTel(self, value):
        self._tel = value

    def setPassword(self, value):
        self._password = value

    def setLogin(self, value):
        self._login = value

    def setNom(self, value):
        self._nom = value

    def setPrenom(self, value):
        self._prenom = value

    def setNationalite(self, value):
        self._nationalite = value

    def setEmail(self, value):
        self._email = value
