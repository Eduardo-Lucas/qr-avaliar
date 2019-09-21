from django import forms

from apps.perguntas.models import Pergunta


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['texto_da_pergunta', ]
