from django.urls import path
from .views import Searcher,Pacient_Info,LungMostRecent, HeartMostRecent,Allinfo,LungBetweenDates,HeartBetweenDates,InfoByDate,HeartBetweenValues,LungBetweenValues,ExportDataView,ChartView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('Searcher/', Searcher, name='Searcher'),
    path('Pacient_Info/<str:paciente_nome>/', Pacient_Info, name='Pacient_Info'),
    path('HeartMostRecent/<str:paciente_cpf>/', HeartMostRecent, name='HeartMostRecent'),
    path('Allinfo/<str:paciente_cpf>/', Allinfo, name='Allinfo'),
    path('HeartBetweenDates/<str:paciente_cpf>/', HeartBetweenDates, name='HeartBetweenDates'),
    path('LungBetweenDates/<str:paciente_cpf>/', LungBetweenDates, name='LungBetweenDates'),
    path('InfoByDate/', InfoByDate, name='InfoByDate'),
    path('HeartBetweenValues/<str:paciente_nome>/', HeartBetweenValues, name='HeartBetweenValues'),
    path('LungBetweenValues/<str:paciente_nome>/', LungBetweenValues, name='LungBetweenValues'),
    path('Chart/', ChartView.as_view(), name='Chart'),
    path('ExportData/', ExportDataView.as_view(), name='ExportData'),
    path('LungMostRecent/<str:paciente_cpf>/', LungMostRecent, name='LungMostRecent'),

]