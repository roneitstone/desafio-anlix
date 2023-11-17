from django.shortcuts import render
import sys
sys.path.append("..")
from aplication.models import Paciente
def home(request):
    #todos_objetos = Paciente.objects.all()

# Iterando e imprimindo
  #  for objeto in todos_objetos:
      #  print( objeto.idade )

    return render(request, 'Hospital_Manager/home.html', {'texto': 'Bem-vindo ao Hospital Name_Here!'})

