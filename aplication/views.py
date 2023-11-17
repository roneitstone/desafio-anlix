
from django.shortcuts import render
from .forms import EntranceForm
from django.shortcuts import render
import json
from .models import Paciente,Dado_Car,Dado_Pulm
from django.shortcuts import render, get_object_or_404
import os
from datetime import datetime

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
    datas = []
    
    for data in Dado_car:
        datas.append(data.Epoch)
    # Converter as strings para objetos datetime
    datas_convertidas = [datetime.strptime(data, "%d/%m/%Y %H:%M:%S") for data in datas]

    # Encontrar a data e hora mais recente
    car_recent = max(datas_convertidas)
    car_recent = car_recent.strftime("%d/%m/%Y %H:%M:%S")
    datas = []
    
    for data in Dado_pulm:
        datas.append(data.Epoch)

    datas_convertidas = [datetime.strptime(data, "%d/%m/%Y %H:%M:%S") for data in datas]


    pulm_recent = max(datas_convertidas)
    pulm_recent = pulm_recent.strftime("%d/%m/%Y %H:%M:%S")


    Dado_car = get_object_or_404(Dado_Car, Epoch = car_recent)
    Dado_pulm = get_object_or_404(Dado_Pulm, Epoch =pulm_recent)

    return render(request, './Hospital_Manager/MostRecent.html', {'Indice_car': str(Dado_car.Ind_Card),  'Indice_pulm':str(Dado_pulm.Ind_Pulm)})
