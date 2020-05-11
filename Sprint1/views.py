from django.http import HttpResponse


def index(request):
    return HttpResponse("Index de Sprint 1")
