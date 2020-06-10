from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from Sprint1.models.utilisateur import Utilisateur
from django.db import models


class Desserte(Utilisateur):
    """docstring for Desserte"""

    tel = models.CharField(max_length=20, null=False)

    @staticmethod
    def authentification(login, password):
        from Sprint1.models import Admin, client, desserte, accueil
        user = authenticate(username=login, password=password)
        if user:
            id = user.id
            u = Desserte.objects.filter(user_id=id)
            if u.count() > 0:
                return u[0]
        return None

    @staticmethod
    def inscription(username, email, password, dateNaissance=None, nationalite="", profession="", tel=""):
        if Utilisateur.exist(username):
            return False

        user = User.objects.create_user(username, email, password)

        u = Desserte(user=user, dateNaissance=dateNaissance, nationalite=nationalite, profession=profession,
                     tel=tel)
        user.save()
        u.save()
        return True

    def donnerNote(self, article, note):
        pass

    # mutateurs et accesseurs
    def getTel(self):
        return self.tel

    def setTel(self, value):
        self.tel = value