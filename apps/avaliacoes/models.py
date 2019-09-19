from django.db import models

from apps.eventos.models import Evento
from apps.perguntas.models import Pergunta

TIPO_RESPOSTA = (
        ('Botão', 'Botão'),
        ('Texto', 'Texto')
    )


class Avaliacao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15, choices=TIPO_RESPOSTA, default='Botão')
    ordem = models.PositiveIntegerField(default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['ordem']
        unique_together = ['evento', 'pergunta']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        
    def __str__(self):
        return str(self.evento) + ' - ' + str(self.pergunta)
