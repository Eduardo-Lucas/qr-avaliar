from django.db import models

from apps.perguntas.models import Pergunta
from apps.respostas_padroes.models import RespostaPadrao


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao = models.ForeignKey(RespostaPadrao, on_delete=models.CASCADE)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.opcao
    
    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
