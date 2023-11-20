
from django.contrib import admin
from django.urls import path, include
from aplication.views import  SearcherApiViewSet
from rest_framework import routers
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'search', SearcherApiViewSet, basename='search')

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('aplication/', include("aplication.urls")),
]
