from Sprint1.models.utilisateur import Utilisateur


class Admin(Utilisateur):
    """docstring for Admin"""

    def __del__(self):
        Utilisateur.__del__(self)

    def __init__(self, login, password, tel="", poste=""):
        Utilisateur.__init__(self, login, password)
        self._tel = tel
        self._poste = poste

    @staticmethod
    def authentification(self, login, password):
        Utilisateur.authentification(self, login, password)

    def inscription(self,log,pwd, userTab):
        if (self.exist(userTab) != True):
            print("") # requete SQL
        else :
            print("Vous etes deja presant dans BD")

    def exist(self,userTab):
        Utilisateur.exist(self, userTab)

    def supprimer(self):
        pass

    def modifier(self):
        pass

    # mutateurs et accesseurs
    def getTel(self):
        return self._tel

    def getPoste(self):
        return self._poste

    def setTel(self, value):
        self._tel = value

    def setPoste(self, value):
        self._poste = value
