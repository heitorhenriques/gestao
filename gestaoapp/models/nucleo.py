from django.db import models
from gestaoapp.models.usuario import Usuario
from django.contrib.auth.models import User


class Nucleo(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=5)
    descricao = models.TextField()
    data_hora_cadastro = models.DateTimeField(auto_now=True)
    responsavel_cadastro = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome
