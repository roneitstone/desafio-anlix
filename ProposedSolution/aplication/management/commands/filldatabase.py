from django.core.management.base import BaseCommand, CommandParser
from aplication.models import Paciente, Dado_Car, Dado_Pulm
import json
import os
from datetime import datetime, timezone, timedelta
from django.utils import timezone

class Command(BaseCommand):
  #  help = "import Booms"

    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):

      if(os.name == "nt"):
            nome_arquivo = '..\dados\pacientes.json'
      else:
            nome_arquivo = '../dados/pacientes.json'
        # Obtém a lista de arquivos na pasta  

      with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
          dados_json = json.load(arquivo)


 

      if isinstance(dados_json, list):
        for pessoa in dados_json:
          for chave,valor in pessoa.items():
            if(chave == "nome"):
              nome = valor
            if(chave == "idade"):
              idade = valor
            if(chave == "cpf"):
              cpf = valor
            if(chave == "rg"):
              rg = valor
            if(chave == "data_nasc"):
              data_nasc = valor
            if(chave == "sexo"):
              sexo =valor
            if(chave == "signo"):
              signo=valor
            if(chave == "mae"):
              mae=valor
            if(chave == "pai"):
              pai=valor
            if(chave == "email"):
              email=valor
            if(chave == "senha"):
              senha=valor
            if(chave == "cep"):
              cep=valor
            if(chave == "endereco"):
              endereco=valor
            if(chave == "numero"):
              numero=valor
            if(chave == "bairro"):
              bairro=valor
            if(chave == "cidade"):
              cidade=valor
            if(chave == "estado"):
              estado=valor
            if(chave == "telefone_fixo"):
              telefone_fixo=valor
            if(chave == "celular"):
              celular=valor
            if(chave == "altura"):
              altura=valor
            if(chave == "peso"):
              peso=valor
            if(chave == "tipo_sanguineo"):
              tipo_sanguineo=valor
            if(chave == "cor"):
              cor=valor       
                      
          models = Paciente(nome = nome,idade = idade,cpf = cpf,rg = rg,data_nasc = data_nasc,sexo =sexo,signo=signo,
                              mae=mae,pai=pai,email=email,senha=senha,cep=cep,endereco=endereco,numero=numero,bairro=bairro,
                              cidade=cidade,estado=estado,telefone_fixo=telefone_fixo,celular=celular,altura=altura,peso=peso,tipo_sanguineo=tipo_sanguineo,
                              cor=cor )
          models.save()
      # populando o database com os valores
      lista_dados = []
      if(os.name == "nt"):
            caminho_pasta = '..\dados\indice_cardiaco'
      else:
            caminho_pasta = '../dados/indice_cardiaco'
        # Obtém a lista de arquivos na pasta
      for nome_arquivo in os.listdir(caminho_pasta):
        caminho_absoluto = os.path.join(caminho_pasta, nome_arquivo)
                  # Verifica se é um arquivo
        if os.path.isfile(caminho_absoluto):
          with open(caminho_absoluto, 'r', encoding='utf-8') as f:
            dados_arquivo = f.readlines()
            dados_arquivo=dados_arquivo[1:]
            lista_dados.append(dados_arquivo)

      i=0
      for dados in lista_dados:
        for aux2 in dados:
          aux2=aux2.rstrip("\n")
          aux= aux2.split(" ")
          # Criar um objeto datetime a partir do valor de época
          dt = datetime.fromtimestamp(int(aux[1]), tz=timezone.utc)
          dt_sao_paulo = dt -timedelta(hours=3)


          indi = Dado_Car(data = dt_sao_paulo, Ind_Card=aux[2], Epoch=int(aux[1]), cpf=aux[0])
          indi.save()
        i+=1

      lista_dados = []
      if(os.name == "nt"):
        caminho_pasta = '..\dados\indice_pulmonar'
      else:
        caminho_pasta = '../dados/indice_pulmonar'

            # Obtém a lista de arquivos na pasta
      for nome_arquivo in os.listdir(caminho_pasta):
        caminho_absoluto = os.path.join(caminho_pasta, nome_arquivo)

        # Verifica se é um arquivo
        if os.path.isfile(caminho_absoluto):
          with open(caminho_absoluto, 'r', encoding='utf-8') as f:
            dados_arquivo = f.readlines()
            dados_arquivo=dados_arquivo[1:]
            lista_dados.append(dados_arquivo)


      i=0           
      for dados in lista_dados:
        for aux2 in dados:
          aux2=aux2.rstrip("\n")
          aux= aux2.split(" ")
          #  Criar um objeto datetime a partir do valor de época
          dt = datetime.fromtimestamp(int(aux[1]), tz=timezone.utc)
          
          dt_sao_paulo = dt -timedelta(hours=3)
          
          indi2 = Dado_Pulm(data = dt_sao_paulo,Ind_Pulm=aux[2], Epoch=int(aux[1]), cpf=aux[0])
          indi2.save()
        i+= 1
# demorou 1.40 segundos no meu computador para terminar o populate