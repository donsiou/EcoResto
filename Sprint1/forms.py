from django import forms


class ConnexionForm(forms.Form):
    login = forms.CharField(label="Nom d'utilisateur", max_length=30)
    mdp = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)