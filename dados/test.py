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
 