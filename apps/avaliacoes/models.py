from django.db import models

from apps.eventos.models import Evento
from apps.perguntas.models import Pergunta


class Avaliacao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['evento', 'pergunta']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        
    def __str__(self):
        return str(self.evento) + ' - ' + str(self.pergunta)
