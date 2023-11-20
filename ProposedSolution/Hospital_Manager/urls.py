from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .view import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('aplication/', include('aplication.urls')),

]
