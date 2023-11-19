from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .view import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aplication/', include('aplication.urls')),

]
