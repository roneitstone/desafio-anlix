
from django.shortcuts import render,redirect
from .forms import EntranceForm
from django.shortcuts import render
from .models import Paciente,Dado_Car,Dado_Pulm
from django.shortcuts import render, get_object_or_404
import os
from .forms import BetweenDatesForm, InfoByDateForm, BetweenValuesForm,ChartForm, ExportForm
from django.urls import reverse
from datetime import datetime
from django.views import View
import json
import csv
from django.http import HttpResponse
from django.views import View

# funcoes auxiliares
 

def acharmaisrecente(resultado):
    aux = [];
    auxepoch = []
    index =0;
    for i in resultado:
        aux = i.split(" ")
        auxepoch.append(int(aux[1]))
    

    # ele acha o maior numero, busca seu indice na lista que recebemos e depois cortamos o string 
    index = resultado[auxepoch.index(max(auxepoch))].split(" ")
    index = index[2]
    return index;

def ler_arquivos_em_pasta(caminho_pasta, cpf, lista):
    
    # Obtém a lista de arquivos na pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_absoluto = os.path.join(caminho_pasta, nome_arquivo)
        lista = converter_e_pesquisar(caminho_absoluto, cpf, lista)

    return lista

def converter_e_pesquisar(nome_arquivo, string_pesquisa, linhas_examinadas):

    # Converte o arquivo não rastreado para .txt
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_original:
        linhas = arquivo_original.readlines()
        with open('arquivo_convertido.txt', 'w', encoding='utf-8') as arquivo_txt:
            arquivo_txt.writelines(linhas)

    # Pesquisa as ocorrências da string linha a linha
    with open('arquivo_convertido.txt', 'r', encoding='utf-8') as arquivo_txt:
        for linha in arquivo_txt:
            if string_pesquisa in linha:
                linhas_examinadas.append(linha.strip())

    return linhas_examinadas

# Função para encontrar todas as chaves e valores associados a um nome
def encontrar_chaves_e_valores(nome_procurado,data):
    for elemento in data:
        if isinstance(elemento, dict) and "nome" in elemento and elemento["nome"] == nome_procurado:
            return elemento.items()
    return None



def Entrance(request):
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário aqui
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
 
            # Redirecione ou renderize outra página
    else:
        form = EntranceForm()

    return render(request, './Hospital_Manager/Entrance.html', {'form': form})

#vamos mudar bastante aq
def Buscador(request):
    
    nome_pesquisado = request.GET.get('palavra', '')
    temp = nome_pesquisado.split("%20")
    nome_pesquisado = " ".join(temp)
    pacientes_encontrados = Paciente.objects.filter(nome__icontains=nome_pesquisado)

    # Extrai os nomes dos pacientes encontrados
    nomes_pacientes = [paciente.nome for paciente in pacientes_encontrados]

 
    return render(request, './Hospital_Manager/Buscador.html', { 'resultados': nomes_pacientes})

def Detalhes_Paciente(request, paciente_nome):

    paciente = get_object_or_404(Paciente, nome=paciente_nome)
    print(paciente.nome)
    return render(request, './Hospital_Manager/Detalhes_Paciente.html', {'paciente': paciente})

def MostRecent (request, paciente_cpf):
    Dado_car = Dado_Car.objects.filter(cpf__icontains=paciente_cpf)

    Dado_pulm = Dado_Pulm.objects.filter(cpf__icontains=paciente_cpf)
     
 

    Dado_car = get_object_or_404(Dado_Car, Epoch = Dado_car[0].Epoch)
    Dado_pulm = get_object_or_404(Dado_Pulm, Epoch =Dado_pulm[0].Epoch)

    return render(request, './Hospital_Manager/MostRecent.html', {'Indice_car': str(Dado_car.Ind_Card),  'Indice_pulm':str(Dado_pulm.Ind_Pulm)})

def Allinfo (request, paciente_cpf):
    
   
    objetoscar = Dado_Car.objects.filter(cpf=paciente_cpf)
    objetospulm = Dado_Pulm.objects.filter(cpf=paciente_cpf)
    


    return render(request, './Hospital_Manager/Allinfo.html', {'objetosCar': objetoscar, 'objetosPulm': objetospulm})

def BetweenDates(request, paciente_cpf):
    
    objetoscar = Dado_Car.objects.filter(cpf=paciente_cpf)
    objetospulm = Dado_Pulm.objects.filter(cpf=paciente_cpf)
    if request.method == 'POST':
        form = BetweenDatesForm(request.POST)
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        aux=[]
        # Converte as strings para objetos datetime
        data_1 = datetime.strptime(start_date, "%Y-%m-%d")
        data_2 = datetime.strptime(end_date, "%Y-%m-%d")
        if(data_1 > data_2):
            data_2, data_1 = data_1, data_2
        start_date = data_1.strftime('%Y-%m-%d')
        end_date = data_2.strftime('%Y-%m-%d')
        aux = start_date.split("-")
        datainit = datetime(int(aux[0]), int(aux[1]), int(aux[2]),0,0,0)
        aux = end_date.split("-")
        dataend = datetime(int(aux[0]), int(aux[1]),int(aux[2]),23,59,59)

        if(datainit> dataend):
            print("entrou")

            objetoscar = objetoscar .filter(data__range=[dataend, datainit])
            objetospulm = objetospulm.filter(data__range=[dataend, datainit])
        else:
            objetoscar = objetoscar .filter(data__range=[datainit, dataend])
            objetospulm = objetospulm.filter(data__range=[datainit, dataend])

    else:
        form = BetweenDatesForm()

        # Usei reverse para construir a URL reversa de forma dinâmica
    form_action_url = reverse('BetweenDates', args=[paciente_cpf])

    return render(request, 'Hospital_Manager/BetweenDates.html', {'objetosCar': objetoscar, 'objetosPulm': objetospulm, 'form': form, 'paciente_cpf': paciente_cpf, 'form_action_url': form_action_url})

def InfoByDate(request):
    objetoscar = []
    objetospulm = []
    if request.method == 'POST':
        form = InfoByDateForm(request.POST)
        start_date = request.POST.get("date")
        end_date = start_date
        aux=[]
        aux = start_date.split("-")
        datainit = datetime(int(aux[0]), int(aux[1]), int(aux[2]),0,0,0)
        aux = end_date.split("-")
        dataend = datetime(int(aux[0]), int(aux[1]),int(aux[2]),23,59,59)
    
        objetoscar = Dado_Car.objects.filter(data__range=[datainit, dataend])
        objetospulm = Dado_Pulm.objects.filter(data__range=[datainit, dataend])
        print(objetoscar)
    else:
        form = InfoByDateForm()

        # Usei reverse para construir a URL reversa de forma dinâmica
    form_action_url = reverse('InfoByDate')
    return render(request, 'Hospital_Manager/InfoByDate.html', {'objetosCar': objetoscar, 'objetosPulm': objetospulm, 'form': form, 'form_action_url': form_action_url})

def CardBetweenValues(request, paciente_nome):
    paciente = get_object_or_404(Paciente, nome = paciente_nome)
    paciente_cpf = paciente.cpf
    print(paciente_cpf)
    objetoscar = Dado_Car.objects.filter(cpf=paciente_cpf)
    if request.method == 'POST':
        form = BetweenValuesForm(request.POST)
        start = request.POST.get("start")
        end = request.POST.get("end")


        if(start > end):
            start,end = end,start

        objetoscar = objetoscar .filter(Ind_Card__range=[(start), (end)])

    else:
        form = BetweenValuesForm()

        # Usei reverse para construir a URL reversa de forma dinâmica
    form_action_url = reverse('CardBetweenValues', args=[paciente_nome])
    
    return render(request, 'Hospital_Manager/CardBetweenValues.html', {'objetosCar': objetoscar, 'form': form, 'paciente_nome': paciente_nome, 'form_action_url': form_action_url})

def LungBetweenValues(request, paciente_nome):
    paciente = get_object_or_404(Paciente, nome = paciente_nome)
    paciente_cpf = paciente.cpf
    
    objetospulm = Dado_Pulm.objects.filter(cpf=paciente_cpf)
    if request.method == 'POST':
        form = BetweenValuesForm(request.POST)
        start = request.POST.get("start")
        end = request.POST.get("end")


        if(start > end):
            start,end = end,start

        objetospulm = objetospulm.filter(Ind_Pulm__range=[start, end])

    else:
        form = BetweenValuesForm()

        # Usei reverse para construir a URL reversa de forma dinâmica
    form_action_url = reverse('LungBetweenValues', args=[paciente_nome])
    
    return render(request, 'Hospital_Manager/LungBetweenValues.html', { 'objetosPulm': objetospulm, 'form': form, 'paciente_nome': paciente_nome, 'form_action_url': form_action_url})


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
            print(opcao_selecionada)
            paciente = get_object_or_404(Paciente, nome=nome_selecionado)
            paciente_cpf = paciente.cpf

            if opcao_selecionada == "cardiaco":
                objetoscar = Dado_Car.objects.filter(cpf=paciente_cpf)
                print(objetoscar)
                lista_ind = list(objetoscar.values_list('Ind_Card', flat=True))
                print(lista_ind)

                lista_tempo = list(objetoscar.values_list('data', flat=True))
            elif opcao_selecionada == "pulmonar":
                objetospulm = Dado_Pulm.objects.filter(cpf=paciente_cpf)
                lista_ind = list(objetospulm.values_list('Ind_Pulm', flat=True))
                lista_tempo = list(objetospulm.values_list('data', flat=True))
            print(lista_tempo)
            # Criar uma lista de dicionários
            dados_grafico = []
            #$for tempo, valor_float in zip(lista_tempo, lista_ind):
           #     dados_grafico.append({'tempo': tempo.strftime('%Y/%m/%d %H:%M:%S'), 'valor_float': valor_float})

            # Converter a lista de dicionários para JSON
            #dados_grafico_json = json.dumps(dados_grafico)
            context = {
                "labels": lista_tempo,
                "values": lista_ind,
                "form" : form
                }
            #print(dados_grafico_json)
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form})

class ExportDataView(View):
    template_name = "Hospital_Manager/ExportData.html"

    def get(self, request, *args, **kwargs):
        form = ExportForm()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request, *args, **kwargs):
        form = ExportForm(request.POST)
        # Inicializar listas para armazenar dados
        dados_car = []
        dados_pulm = []

        if form.is_valid():
            # Processar os dados do formulário
            pacientes_selecionados = form.POST.get('pacientes')

            for paciente in pacientes_selecionados:
                dados_car.extend(Dado_Car.objects.filter(cpf=paciente.cpf))
                dados_pulm.extend(Dado_Pulm.objects.filter(cpf=paciente.cpf))


            # Redirecione para a página desejada após processar os dados
            return render(request, self.template_name, {'dados_car': dados_car, 'dados_pulm': dados_pulm})

        return render(request, self.template_name, {'form': form})