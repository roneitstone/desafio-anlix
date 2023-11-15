from django.shortcuts import render
from .forms import EntranceForm
from django.shortcuts import render
import json
from fuzzywuzzy import process
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


def home(request):
    return render(request, 'Hospital_Manager/home.html', {'texto': 'Bem-vindo ao Hospital Name_Here!'})

def Entrance(request):
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário aqui
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            # Faça o que quiser com os dados

            # Redirecione ou renderize outra página
    else:
        form = EntranceForm()

    return render(request, './Hospital_Manager/Entrance.html', {'form': form})


def Buscador(request):
    # Nome do arquivo JSON
    nome_arquivo = 'dados\pacientes.json'

    # Carregar o conteúdo do arquivo JSON
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_json = json.load(arquivo)

    # Chave específica que você está procurando (por exemplo, 'nome')
    chave_procurada = 'nome'
    palavra_escrita = request.GET.get('palavra', '').lower()

    string_concatenada = [];

    # Verificar se a chave 'nome' existe no JSON
    if isinstance(dados_json, list):
        # Se for uma lista, percorrer os itens e imprimir o valor da chave
        listnomes = []
        temp = palavra_escrita.split("%20")
        palavra_escrita = " ".join(temp)

        for item in dados_json:
            if chave_procurada in item:
                valor_da_chave = item[chave_procurada]
                valor_da_chave = valor_da_chave.lower()
                print(valor_da_chave)
                listnomes.append(valor_da_chave.split(" "))

                if(palavra_escrita == valor_da_chave):
                    
                    #evita que o string sozinho seja separado em caracteres pelo .html
                    listnomes.clear()
                    listnomes.append(valor_da_chave)
                    listnomes.append("")

                    return render(request, './Hospital_Manager/Buscador.html', { 'resultados': listnomes})
                
        for i in listnomes:
            for o in i:
                semelhantes =process.extractBests(palavra_escrita, i, score_cutoff=70)
                
                if(semelhantes != []):
                    string_concatenada.append(" ".join(i));
                    break
        #print(f"Palavras semelhantes a {string_concatenada}")
         # Renderizar o template com os resultados
    return render(request, './Hospital_Manager/Buscador.html', { 'resultados': string_concatenada})

