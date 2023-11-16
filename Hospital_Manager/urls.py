from django.contrib import admin
#from .view import Entrance
from django.urls import path
from django.conf.urls import include
from .view import home
#from .view import Buscador


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
 #   path('Entrance/', Entrance, name="Entrance"),
#    path('Buscador/', Buscador, name='Buscador'),
    path('aplication/', include('aplication.urls')),


]
