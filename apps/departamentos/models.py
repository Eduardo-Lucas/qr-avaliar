from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nome', 'empresa')

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('departamento_list')
