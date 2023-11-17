
from django.shortcuts import render
from .forms import EntranceForm
from django.shortcuts import render
import json
from .models import Paciente
from django.shortcuts import render, get_object_or_404
import os

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