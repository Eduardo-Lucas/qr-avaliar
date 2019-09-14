from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class Pergunta(models.Model):
    texto_da_pergunta = models.CharField(validators=[MinLengthValidator(10)], max_length=200, unique=True)
    data_de_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    
    def __str__(self):
        return self.texto_da_pergunta
        
    def get_absolute_url(self):
        return reverse('pergunta_detail',  args=[str(self.pk)])
    
    class Meta:
        ordering = ['texto_da_pergunta']
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
