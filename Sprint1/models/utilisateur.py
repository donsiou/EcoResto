from django.db import models
from datetime import date


class Utilisateur(models.Model):
    """docstring for Utilisateur"""
    _password = models.CharField(max_length=100, null=False, blank=False)
    _login = models.CharField(max_length=100, unique=True, blank=False, null=False)
    _nom = models.CharField(max_length=100, null=False, blank=False)
    _prenom = models.CharField(max_length=100, null=False, blank=False)
    _dateNaissance = models.DateField(null=False, blank=False)
    _dateInscription = models.DateField(null=False, default=date.today())
    _nationalite = models.CharField(max_length=100)
    _email = models.EmailField(max_length=255, null=False, blank=False)
    _profession = models.CharField(max_length=100)

    def __del__(self):
        print("je suis le destructeur")

    # constructeur par defeaut c'est le  mm que par initalization 2 on 1
    def __init__(self, login="", password="", nom="", prenom="", nationalite="", email=""):
        self._password = password
        self._login = login
        self._nom = nom
        self._prenom = prenom
        self._nationalite = nationalite
        self._email = email
        self._profession = profession
        self._tel = tel

    # comme constructeur par recopie

    def clone(self, u):
        self._password = u._password
        self._login = u._login
        self._nom = u._nom
        self._prenom = u._prenom
        self._nationalite = u._nationalite
        self._email = u._email
        self._profession = u._profession
        self._tel = u._tel

    @staticmethod
    def authentification(self, login, password):
        pass

    def inscription(self):
        raise  # ( ' methode abstraite ' )

    def exist(self, tabUsers):
        for u in tabUsers:
            if self._login == u.getLogin() and self._password == u.getPassword():
                return True
            else:
                return False

    def supprimer(self, tabUser):
        i = 0
        for u in tabUser:

            if self.exist(tabUser):
                tabUser.pop(i)
                return True
            else:
                return False
            i = i + 1

    def modifier(self):
        pass

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
