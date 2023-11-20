from .models import Paciente
from django import forms

# forms para a tela do grafico
class ChartForm(forms.Form):
    nomes = Paciente.objects.values_list('nome', flat=True)
    nome_choices = [(nome, nome) for nome in nomes]

    nome = forms.ChoiceField(choices=nome_choices, label='Selecione o Nome')
    opcao = forms.ChoiceField(choices=[('pulmonar', 'Pulmonar'), ('cardiaco', 'Cardíaco')], label='Selecione a Opção')

# forms da tela de export
class ExportForm(forms.Form):
    pacientes = forms.MultipleChoiceField(
        choices=[(paciente.cpf, paciente.nome) for paciente in Paciente.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )