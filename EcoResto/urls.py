"""EcoResto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Sprint1 import views

urlpatterns = {
    path('', include('Sprint1.urls'), name='home'),
    path('index',views.index),
    path('admin/', admin.site.urls),
    path('sprint1/', include('Sprint1.urls')),
    path('Login',views.Login,name='Login'),
    path('Register',views.Register,name='Register'),
    path('inscription',views.inscription,name='inscription'),
}
