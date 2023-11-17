import os


lista_dados = []
caminho_pasta = 'dados\indice_cardiaco'
  # Obtém a lista de arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
  caminho_absoluto = os.path.join(caminho_pasta, nome_arquivo)

            # Verifica se é um arquivo
  if os.path.isfile(caminho_absoluto):
    with open(caminho_absoluto, 'r', encoding='utf-8') as f:
      dados_arquivo = f.readlines()
      dados_arquivo=dados_arquivo[1:]
      lista_dados.append(dados_arquivo)
      

        
for dados in lista_dados:
    for aux in dados:
      aux=aux.rstrip("\n")
      aux2= aux.split(" ")
      print(aux2[0])
print("\n\n\n\n quase la! \n\n\n\n\n\n")
#vamos mudar bastante aq
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
               # print(semelhantes)
                if(semelhantes != []):
                    string_concatenada.append(" ".join(i));
                    break
  
    return render(request, './Hospital_Manager/Buscador.html', { 'resultados': string_concatenada})
