from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Utilisateur(models.Model):
    """docstring for Utilisateur"""
    _password = models.CharField(max_length=100, null=False, blank=False)
    _login = models.CharField(max_length=100, unique=True, blank=False, null=False)
    _nom = models.CharField(max_length=100, null=False, blank=False)
    _prenom = models.CharField(max_length=100, null=False, blank=False)
    _dateNaissance = models.DateField(null=False, blank=False)
    _dateInscription = models.DateField(null=False, default=timezone.now)
    _nationalite = models.CharField(max_length=100)
    _email = models.EmailField(max_length=255, null=False, blank=False)
    _profession = models.CharField(max_length=100)



    #@staticmethod
    def authentification(self, request, login=None, password=None):
        try:
            user= Utilisateur.objects.get(_email=login)
            if user.check_password(password):
                return user
            else :
                return None
        except Utilisateur.DoesNotExist:
            raise ValidationError("Infos fourni erronée")

    def get_user(self, id):
        try:
            return Utilisateur.objects.get(pk=id)
        except Utilisateur.DoesNotExist:
            return None

    def inscription(self):
        raise  # ( ' methode abstraite ' )





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
