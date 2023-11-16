from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=13)
    data_nasc = models.CharField(max_length=12)
    sexo = models.CharField(max_length=9)
    signo = models.CharField(max_length=25)
    mae = models.CharField(max_length=250)
    pai = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    senha = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=250)
    numero = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone_fixo = models.CharField(max_length=14)
    celular = models.CharField(max_length=15)
    altura = models.CharField(max_length=4)
    peso = models.IntegerField()
    tipo_sanguineo = models.CharField(max_length=3)
    cor = models.CharField(max_length=20)
 
    def __str__(self):
        return self.nome 
        
class Dado_Pulm(models.Model):
    Ind_Pulm = models.FloatField();
    Epoch = models.CharField(max_length=10)
    cpf = models.ForeignKey(Paciente, on_delete=models.CASCADE);

class Dado_Car(models.Model):
    Ind_Card = models.FloatField();
    Epoch = models.CharField(max_length=10)
    cpf = models.ForeignKey(Paciente, on_delete=models.CASCADE);
