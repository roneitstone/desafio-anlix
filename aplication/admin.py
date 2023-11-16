from django.contrib import admin
from .models import Paciente
from .models import Dado_Car
from .models import Dado_Pulm

admin.site.register(Paciente)
admin.site.register(Dado_Car)
admin.site.register(Dado_Pulm)

# Register your models here.
