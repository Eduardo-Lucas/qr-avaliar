from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    """Manutenção do Cadastro de Empresas"""
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    
    def __str__(self):
        return self.nome
    
    @staticmethod
    def get_absolute_url():
        return reverse('home')
