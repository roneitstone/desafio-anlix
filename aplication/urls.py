from django.urls import path
from .views import Buscador,Entrance
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('Entrance/', Entrance, name="Entrance"),
    path('Buscador/', Buscador, name='Buscador'),
]