from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms

from apps.eventos.models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data_inicio', 'data_termino', 'descricao', 'publico_privado', 'local', 'cep', 'endereco',
                  'numero', 'bairro', 'cidade', 'uf', 'absorver_taxa_servico']
        widgets = {
            'data_inicio': DateTimePickerInput(options={
                                                   'format': '%d/%m/%Y %H:%M',
                                                   'showClose': True,
                                                   'showClear': True,
                                                   'showTodayButton': True,
                                               })
        }
