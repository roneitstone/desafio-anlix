from django.urls import path
from .views import Buscador,Entrance,Detalhes_Paciente, MostRecent
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('Entrance/', Entrance, name="Entrance"),
    path('Buscador/', Buscador, name='Buscador'),
    path('Detalhes_Paciente/<str:paciente_nome>/', Detalhes_Paciente, name='Detalhes_Paciente'),
    path('MostRecent/<str:paciente_cpf>/', MostRecent, name='MostRecent'),

]