from django.shortcuts import render
import sys
sys.path.append("..")
from aplication.models import Paciente
def home(request):

    return render(request, 'Hospital_Manager/home.html', {'texto': 'Bem-vindo ao Hospital Name_Here!'})

