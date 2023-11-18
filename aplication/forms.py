 
from django import forms

class EntranceForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')



class BetweenDatesForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),input_formats=['%Y/%m/%d'])
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y/%m/%d'])
