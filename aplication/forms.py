from .models import Paciente
from django import forms

class EntranceForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')



class BetweenValuesForm(forms.Form):
    end = forms.FloatField(label='Maior Valor')
    start = forms.FloatField(label='Menor Valor')

class BetweenDatesForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),input_formats=['%Y/%m/%d'])
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y/%m/%d'])

class InfoByDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),input_formats=['%Y/%m/%d'])


class ChartForm(forms.Form):
    nomes = Paciente.objects.values_list('nome', flat=True)
    nome_choices = [(nome, nome) for nome in nomes]

    nome = forms.ChoiceField(choices=nome_choices, label='Selecione o Nome')
    opcao = forms.ChoiceField(choices=[('pulmonar', 'Pulmonar'), ('cardiaco', 'Cardíaco')], label='Selecione a Opção')

class ExportForm(forms.Form):
    pacientes = forms.MultipleChoiceField(
        choices=[(paciente.id, paciente.nome) for paciente in Paciente.objects.all()],
        widget=forms.CheckboxSelectMultiple,
    )