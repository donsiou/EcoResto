from django.contrib.auth.views import LoginView
from django.urls import path
from Sprint1 import views

urlpatterns = [
    # path('', views.index),
    path(r'^$', views.login),
    # path(r'^accounts/logout/$', views.logout),
]
