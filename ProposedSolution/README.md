# Desafio Anlix

 
**Sobre o desafio**

Os arquivos texto localizados no diretório dados apresentam diversas características sobre pacientes terminais internados em um hospital, que  são fornecidos por áreas distintas e sempre serão fornecidos separadamente. Os arquivos texto fornecidos por uma mesma área estão nomeados com datas distintas, pois retratam características dos pacientes em diferentes dias. Precisamos que você crie um software que contenha uma base de dados consultável através de uma API REST capaz de:

* [X] Buscar um paciente por nome e exibir o valor mais recente de cada uma de suas características;
```bash
localhost:PORT/aplication/mostrecent/NomeDoPaciente/Tipo    
# Example : 
localhost:PORT/aplication/mostrecent/Alexandre Caleb Costa/cardiaco
```

* [X] Consultar em uma única chamada, todas as características de um paciente, com os valores mais recentes de cada uma;
```bash
localhost:PORT/aplication/allinfo/Patient_CPF/
#Example : 
localhost:PORT/aplication/allinfo/974.642.524-20/
```

* [X] Consultar para uma determinada data (dia, mês e ano), todas as características existentes de todos os pacientes da base de dados;
```bash
$localhost:PORT/aplication/InfoByDate$
```

* [X] Consultar uma característica qualquer de um paciente para um intervalo de datas a ser especificado na chamada da API;
```bash
localhost:PORT/aplication/heartbetweendates/Patient_CPF/Y-M-D_Y-M-D 
localhost:PORT/aplication/lungbetweendates/Patient_CPF/Y-M-D_Y-M-D
#Example : 
localhost:PORT/aplication/lungbetweendates/436.612.686-94/2021-06-21_2021-06-13/
```

* [X] Consultar o valor mais recente de uma característica de um paciente que esteja entre um intervalo de valores a ser especificado na chamada da API;
```bash
localhost:PORT/aplication/heartbetweenvalues/Patient_CPF/value1_value2
localhost:PORT/aplication/lungbetweenvalues/Patient_CPF/value1_value2
#Example : 
http://localhost:PORT/aplication/heartbetweenvalues/436.612.686-94/0.5_0.2
```

* [X] Consultar pacientes que contenham um nome ou parte de um nome a ser especificado na chamada da API.
```bash
localhost:PORT/search/?name=NomeAPesquisar

#Example : 
localhost:PORT/search/?nome=marco
```
* Ser possível exportar as características de um ou mais pacientes de todas as datas disponíveis para um arquivo CSV;
```bash
localhost:PORT/aplication/export/
``` 

* Exibir um gráfico temporal para um determinado paciente e uma determinada característica a ser inserida através da interface.
```bash
localhost:PORT/aplication/chart/
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
Ou 

**Por DockerCompose**
Devido ao popular inserido na linha de comando, pode demorar para executar, sem o docker, a execução é mais rápida.
```bash
docker-compose up
```