from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from apps.empresas.models import Empresa

TIPO_DE_EVENTO_CHOICES = (
    ('PUBLICO', 'Público'),
    ('PRIVADO', 'Privado'),
)


class Evento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, )
    data_inicio = models.DateTimeField(
        _("Data de Início"), auto_now=False, auto_now_add=False)
    data_termino = models.DateTimeField(
        _("Data de Término"), auto_now=False, auto_now_add=False)
    descricao = models.TextField('Descrição do Evento', max_length=100)
    publico_privado = models.CharField(
        max_length=10, choices=TIPO_DE_EVENTO_CHOICES, default='PUBLICO')
    local = models.CharField(max_length=100, )
    cep = models.name = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=100, )
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=25, blank=True, null=True)
    cidade = models.CharField(max_length=25, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    absorver_taxa_servico = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['empresa', 'nome', 'data_inicio']
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("evento_detail", kwargs={"pk": self.pk})
