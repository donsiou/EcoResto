from django.http import HttpResponse


def index(request):
    return HttpResponse("Index de Sprint 1")


def indexPage(request):
    return HttpResponse("<h1>Hello world !</h1>")
