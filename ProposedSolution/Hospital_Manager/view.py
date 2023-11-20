from django.shortcuts import render
import sys
sys.path.append("..")
from aplication.models import Paciente
def Home(request):

    return render(request, 'Hospital_Manager/Home.html', {'texto': 'Bem-vindo!'})

