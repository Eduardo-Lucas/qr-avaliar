from django.db import models
from django.urls import reverse

"""
Valores esperados:
Sim
Não
Péssimo
Ruim
Regular
Bom
Ótimo
0
1
2
3
4
5
6
7
8
9
10
20
25
30
50
75
100
"""


class RespostaPadrao(models.Model):
    texto = models.CharField('Resposta Padrão', max_length=20, unique=True)
    
    def __str__(self):
        return self.texto
    
    def get_absolute_url(self):
        return reverse('resposta_padrao_detail',  args=[str(self.pk)])

    class Meta:
        ordering = ['texto']
        verbose_name = 'Resposta Padrão'
        verbose_name_plural = 'Respostas Padrões'
