from django.http import HttpResponse
from django.template import loader

def redirect(request):
    return redirect(home)
def Login(request):
    template = loader.get_template('Sprint1/login.html')
    return HttpResponse(template.render(request=request))

def Register(request):
    template = loader.get_template('Sprint1/register.html')
    return HttpResponse(template.render(request=request))


def indexOuma(request):
    template = loader.get_template('Sprint1/index.html')
    return HttpResponse(template.render(request=request))


def Ajouter_Article(request):
    template = loader.get_template('Sprint1/GestionArticles_Ajouter.html')
    return HttpResponse(template.render(request=request))


def Articles(request):
    template = loader.get_template('Sprint1/GestionArticles_Afficher.html')
    return HttpResponse(template.render(request=request))





