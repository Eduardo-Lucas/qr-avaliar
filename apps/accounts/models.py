from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import models


class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True, )
    whatsapp = models.CharField(max_length=50, unique=True, )
    email = models.EmailField(validators=[EmailValidator], )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
