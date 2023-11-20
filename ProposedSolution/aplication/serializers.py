from rest_framework import serializers
from .models import Paciente, Dado_Car, Dado_Pulm

# Serializers define the API representation.
class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'cpf', 'rg', 'data_nasc',"sexo","signo","mae","pai","email","senha","cep","endereco","numero",
                  "bairro","cidade","estado","telefone_fixo","celular","altura","peso","tipo_sanguineo","cor"]
class Dado_CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dado_Car
        fields = ['cpf', 'data', 'Epoch', 'Ind_Card']

class Dado_PulmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dado_Pulm
        fields = ['cpf', 'data', 'Epoch', 'Ind_Pulm']
            