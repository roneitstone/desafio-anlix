from django.shortcuts import render,get_object_or_404,HttpResponse
import csv
from django.http import JsonResponse
from .models import Paciente,Dado_Car,Dado_Pulm
from .serializers import PacienteSerializer, Dado_CarSerializer,Dado_PulmSerializer
from rest_framework import viewsets
from datetime import datetime
from django.views import View
from .forms import ChartForm, ExportForm

# Funcao que mostra os dados cardiacos ou pulmonares mais recentes

def MostRecent (request, nome,area):

    if(area == "pulmonar"):

        paciente = get_object_or_404(Paciente, nome =nome)

        Dado_pulm = Dado_Pulm.objects.filter(cpf__icontains=paciente.cpf)
        Dado_pulm = get_object_or_404(Dado_Pulm, Epoch =Dado_pulm[0].Epoch)
        ind = Dado_pulm.Ind_Pulm
    if(area == "cardiaco"):
        paciente = get_object_or_404(Paciente, nome =nome)
        Dado_car = Dado_Car.objects.filter(cpf__icontains=paciente.cpf)
        Dado_car = get_object_or_404(Dado_Car, Epoch = Dado_car[0].Epoch)
        ind = Dado_car.Ind_Card


    return render(request, './Hospital_Manager/MostRecent.html', {  'Indice':str(ind)})

# classe que exporta o csv com os dados dos pacientes selecionados

class ExportDataView(View):
    template_name = "Hospital_Manager/ExportData.html"

    def get(self, request, *args, **kwargs):
        form = ExportForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ExportForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            pacientes_selecionados = form.cleaned_data['pacientes']

            # Criar uma resposta de HTTP com um arquivo CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="ExportedData.csv"'

            # Configurar o escritor CSV
            writer = csv.writer(response)

            # Escrever o cabeçalho
            writer.writerow(['Nome', 'Ind_Card', 'Data_Card', 'Ind_Pulm', 'Data_Pulm'])

            # Iterar sobre os pacientes selecionados
            for paciente_id in pacientes_selecionados:
                # Obter objetos Dado_Car e Dado_Pulm para o paciente
                dados_car = Dado_Car.objects.filter(cpf=paciente_id)
                dados_pulm = Dado_Pulm.objects.filter(cpf=paciente_id)
                paciente = get_object_or_404(Paciente, cpf=paciente_id)
                # Iterar sobre os dados e escrever no CSV
                for dado_car in dados_car:
                    
                    writer.writerow([paciente.nome, dado_car.Ind_Card, dado_car.data, None, None])
                for dado_pulm in dados_pulm:
                    writer.writerow([paciente.nome, None, None, dado_pulm.Ind_Pulm, dado_pulm.data])

            return response

        return render(request, self.template_name, {'form': form})

# Classe usada para gerar o gráfico que mostra todos os dados de uma caracteristica de um paciente

class ChartView(View):
    template_name = "Hospital_Manager/ChartData.html"

    def get(self, request, *args, **kwargs):
        form = ChartForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ChartForm(request.POST)
        objetospulm = Dado_Pulm.objects.all()
        objetoscar = Dado_Car.objects.all()

        lista_tempo = []   
        lista_ind = []

        if form.is_valid():
            nome_selecionado = request.POST.get("nome")
            opcao_selecionada = request.POST.get("opcao")
            paciente = get_object_or_404(Paciente, nome=nome_selecionado)
            paciente_cpf = paciente.cpf

            if opcao_selecionada == "cardiaco":
                objetoscar = Dado_Car.objects.filter(cpf=paciente_cpf)
                lista_ind = list(objetoscar.values_list('Ind_Card', flat=True))

                lista_tempo = list(objetoscar.values_list('data', flat=True))
            elif opcao_selecionada == "pulmonar":
                objetospulm = Dado_Pulm.objects.filter(cpf=paciente_cpf)
                lista_ind = list(objetospulm.values_list('Ind_Pulm', flat=True))
                lista_tempo = list(objetospulm.values_list('data', flat=True))

            # Criar um context com dados
            context = {
                "labels": lista_tempo,
                "values": lista_ind,
                "form" : form
                }
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form})

# Funcao que mostra as caracteristicas pulmonares de um paciente num intervalo de datas

def LungBetweenDates(request,cpf,intervalo):
    
    temp2 = []
    temp2 = intervalo.split("_")
    data_1 = datetime.strptime(temp2[0], "%Y-%m-%d")
    data_2 = datetime.strptime(temp2[1], "%Y-%m-%d")
    
    if(data_1 > data_2):
        data_2, data_1 = data_1, data_2

    start_date = data_1.strftime('%Y-%m-%d')
    end_date = data_2.strftime('%Y-%m-%d')
    aux = start_date.split("-")
    datainit = datetime(int(aux[0]), int(aux[1]), int(aux[2]),0,0,0)
    aux = end_date.split("-")
    dataend = datetime(int(aux[0]), int(aux[1]),int(aux[2]),23,59,59)
    objetospulm = Dado_Pulm.objects.filter(cpf=cpf)

    if(datainit> dataend):
    
        queryset_modelo1 = objetospulm.filter(data__range=[dataend, datainit])

    else:
        queryset_modelo1 = objetospulm.filter(data__range=[datainit, dataend])

    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_PulmSerializer(queryset_modelo1, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Pulmonar': serializer_modelo1.data,
    })

# Funcao que mostra as caracteristicas cardiacas de um paciente num intervalo de datas


def HeartBetweenDates(request,cpf,intervalo):

    temp2 = []
    temp2 = intervalo.split("_")
    data_1 = datetime.strptime(temp2[0], "%Y-%m-%d")
    data_2 = datetime.strptime(temp2[1], "%Y-%m-%d")
    
    if(data_1 > data_2):
        data_2, data_1 = data_1, data_2

    start_date = data_1.strftime('%Y-%m-%d')
    end_date = data_2.strftime('%Y-%m-%d')
    aux = start_date.split("-")
    datainit = datetime(int(aux[0]), int(aux[1]), int(aux[2]),0,0,0)
    aux = end_date.split("-")
    dataend = datetime(int(aux[0]), int(aux[1]),int(aux[2]),23,59,59)
    objetoscar = Dado_Car.objects.filter(cpf=cpf)

    if(datainit> dataend):
    
        queryset_modelo1 = objetoscar.filter(data__range=[dataend, datainit])

    else:
        queryset_modelo1 = objetoscar.filter(data__range=[datainit, dataend])

    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_CarSerializer(queryset_modelo1, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Cardíaco': serializer_modelo1.data,
    })

# Funcao que mostra as caracteristicas pulmonares de um paciente num intervalo de valores

def LungBetweenValues(request, cpf,intervalo):
    
    temp = []
    temp = intervalo.split("_")
    if(temp[0]> temp[1]):
        temp[0],temp[1] = temp[1],temp[0]
    
 

    objetospulm = Dado_Pulm.objects.filter(cpf = cpf)
    queryset_modelo1 = objetospulm.filter(Ind_Pulm__range=[(temp[0]), (temp[1])])

    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_PulmSerializer(queryset_modelo1, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Pulmonar': serializer_modelo1.data,
    })

# Funcao que mostra as caracteristicas cardiacas de um paciente num intervalo de valores

def HeartBetweenValues(request, cpf,intervalo):
    
    temp = []
    
    temp = intervalo.split("_")
    if(temp[0]> temp[1]):
        temp[0],temp[1] = temp[1],temp[0]
    
    

    objetoscar = Dado_Car.objects.filter(cpf = cpf)
    queryset_modelo1 = objetoscar.filter(Ind_Card__range=[(temp[0]), (temp[1])])

    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_CarSerializer(queryset_modelo1, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Cardíaco': serializer_modelo1.data,
    })

# Funcao que mostra todas caracteristicas de todos os pacientes para uma determinada data 

def InfoByDate(request, data):

    aux=[]
    aux = data.split("-")
    datainit = datetime(int(aux[0]), int(aux[1]), int(aux[2]),0,0,0)
    dataend = datetime(int(aux[0]), int(aux[1]),int(aux[2]),23,59,59)
    
    # Realize a pesquisa nos modelos usando o paciente
    queryset_modelo1 = Dado_Car.objects.filter(data__range=[datainit, dataend])
    queryset_modelo2 = Dado_Pulm.objects.filter(data__range=[datainit, dataend])
 
    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_CarSerializer(queryset_modelo1, many=True)
    serializer_modelo2 = Dado_PulmSerializer(queryset_modelo2, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Cardíaco': serializer_modelo1.data,
        'Índice Pulmonar': serializer_modelo2.data,
    })

# Funcao que mostra todas caracteristicas mais recentes de um determinado paciente 

def AllInfo(request, cpf):
    # Obtenha o objeto Paciente correspondente ao CPF
    temp = cpf.split("%20")
    paciente_cpf = " ".join(temp)

    if '/' in paciente_cpf:
        # Divide a string com base na barra e pega apenas a parte antes dela
        temp2 = paciente_cpf.split('/')[0]
        paciente_cpf = temp2

    # Realize a pesquisa nos modelos usando o paciente
    queryset_modelo1 = Dado_Car.objects.filter(cpf=paciente_cpf)
    queryset_modelo2 = Dado_Pulm.objects.filter(cpf=paciente_cpf)
    print(queryset_modelo2)
    # Combine os resultados de ambos os querysets
 
    # Serializa os resultados (usando seus serializadores)
    serializer_modelo1 = Dado_CarSerializer(queryset_modelo1, many=True)
    serializer_modelo2 = Dado_PulmSerializer(queryset_modelo2, many=True)

    # Retorna os resultados serializados como parte da resposta
    return JsonResponse({
        'Índice Cardíaco': serializer_modelo1.data,
        'Índice Pulmonar': serializer_modelo2.data,
    })

# Classe que faz busca e retorna os nomes mais proximos do pesquisado

class SearcherApiViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PacienteSerializer

    def get_queryset(self):
        nome_pesquisado = self.request.query_params.get('nome', '')
        temp = nome_pesquisado.split("%20")
        nome_pesquisado = " ".join(temp)

        if '/' in nome_pesquisado:
            # Divide a string com base na barra e pega apenas a parte antes dela
            temp2 = nome_pesquisado.split('/')[0]
            nome_pesquisado = temp2
        
        queryset = Paciente.objects.filter(nome__icontains=nome_pesquisado)
        return queryset



 