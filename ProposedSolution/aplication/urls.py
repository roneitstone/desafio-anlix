# No arquivo urls.py dentro do diretório do seu aplicativo

from django.urls import path
from .views import AllInfo,InfoByDate,HeartBetweenValues,LungBetweenValues,HeartBetweenDates,LungBetweenDates,MostRecent,ChartView,ExportDataView

urlpatterns = [
    path('allinfo/<str:cpf>/', AllInfo, name='allinfo'),
    path('infobydate/<str:data>/', InfoByDate, name='infobydate'),
    path('heartbetweenvalues/<str:cpf>/<str:intervalo>/', HeartBetweenValues, name='heartbetweenvalues'),
    path('lungbetweenvalues/<str:cpf>/<str:intervalo>/', LungBetweenValues, name='lungbetweenvalues'),
    path('heartbetweendates/<str:cpf>/<str:intervalo>/', HeartBetweenDates, name='heartbetweendates'),
    path('lungbetweendates/<str:cpf>/<str:intervalo>/', LungBetweenDates, name='lungbetweendates'),
    path('chart/', ChartView.as_view(), name='chart'),
    path('export/', ExportDataView.as_view(), name='export'),
    path('mostrecent/<str:nome>/<str:area>/', MostRecent, name='mostrecent'),

]
