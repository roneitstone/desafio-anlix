from django.urls import path
from .views import Buscador,Entrance,Detalhes_Paciente, MostRecent,Allinfo,BetweenDates,InfoByDate,CardBetweenValues,LungBetweenValues,ExportDataView,ChartView
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('Entrance/', Entrance, name="Entrance"),
    path('Buscador/', Buscador, name='Buscador'),
    path('Detalhes_Paciente/<str:paciente_nome>/', Detalhes_Paciente, name='Detalhes_Paciente'),
    path('MostRecent/<str:paciente_cpf>/', MostRecent, name='MostRecent'),
    path('Allinfo/<str:paciente_cpf>/', Allinfo, name='Allinfo'),
    path('BetweenDates/<str:paciente_cpf>/', BetweenDates, name='BetweenDates'),
    path('InfoByDate/', InfoByDate, name='InfoByDate'),
    path('CardBetweenValues/<str:paciente_nome>/', CardBetweenValues, name='CardBetweenValues'),
    path('LungBetweenValues/<str:paciente_nome>/', LungBetweenValues, name='LungBetweenValues'),
    path('Chart/', ChartView.as_view(), name='Chart'),
    path('ExportData/', ExportDataView.as_view(), name='ExportData'),

]