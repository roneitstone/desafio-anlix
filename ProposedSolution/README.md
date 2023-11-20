# Desafio Anlix

 
**Sobre o desafio**

Os arquivos texto localizados no diretório dados apresentam diversas características sobre pacientes terminais internados em um hospital, que  são fornecidos por áreas distintas e sempre serão fornecidos separadamente. Os arquivos texto fornecidos por uma mesma área estão nomeados com datas distintas, pois retratam características dos pacientes em diferentes dias. Precisamos que você crie um software que contenha uma base de dados consultável através de uma API REST capaz de:

* [X] Consultar, para cada paciente, cada uma das características individualmente e cada uma delas sendo a mais recente disponível;
```bash
localhost:PORT/aplication/LungMostRecent/Patient_CPF/  
localhost:PORT/aplication/HeartMostRecent/Patient_CPF/  
# Example : 
localhost:PORT/aplication/LungMostRecent/974.642.524-20/ 
```

* [X] Consultar em uma única chamada, todas as características de um paciente, com os valores mais recentes de cada uma;
```bash
localhost:PORT/aplication/Allinfo/Patient_CPF/
#Example : 
localhost:PORT/aplication/LungMostRecent/974.642.524-20/ 
```

* [X] Consultar para uma determinada data (dia, mês e ano), todas as características existentes de todos os pacientes da base de dados;
```bash
localhost:PORT/aplication/InfoByDate
```

* [X] Consultar uma característica qualquer de um paciente para um intervalo de datas a ser especificado na chamada da API;
```bash
localhost:PORT/aplication/HeartBetweenDates/Patient_CPF/
localhost:PORT/aplication/LungBetweenDates/Patient_CPF/
#Example : 
localhost:PORT/aplication/HeartBetweenDates/974.642.524-20/
```

* [X] Consultar o valor mais recente de uma característica de um paciente que esteja entre um intervalo de valores a ser especificado na chamada da API;
```bash
localhost:PORT/aplication/HeartBetweenValues/Patient_Name/
localhost:PORT/aplication/LungBetweenValues/Patient_Name/
#Example : 
localhost:PORT/aplication/HeartBetweenValues/Alexandre Caleb Costa/
```

* [X] Consultar pacientes que contenham um nome ou parte de um nome a ser especificado na chamada da API.
```bash
localhost:PORT/aplication/Searcher/
```
* Ser possível exportar as características de um ou mais pacientes de todas as datas disponíveis para um arquivo CSV;
```bash
localhost:PORT/aplication/ExportData/
``` 

* Exibir um gráfico temporal para um determinado paciente e uma determinada característica a ser inserida através da interface.
```bash
localhost:PORT/aplication/Chart/
```

**Instruções para inicialização do projeto e utilização**

Instalar o Django and Django-Rest-Framework.
***lembrando que você deve usar o pip presente no seu computador, assim como o python.
Pode ser usado com pip3 e python3 também.***

```bash

pip install django djangorestframework

#Depois de instalar, precisa rodar os seguintes comandos:

#Clonar o diretório

git clone https://github.com/roneitstone/desafio-anlix.git

#Acessar a pasta ProposedSolution

cd ProposedSolution

#Popular a database (Isso pode demorar dependo da potência do servidor)

python manage.py filldatabase

#Quando terminar de popular a database

python manage.py runserver 8000
```
