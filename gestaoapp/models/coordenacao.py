# coding:utf-8
from django.db import models

from gestaoapp.models.usuario import Usuario
from gestaoapp.models.projeto import Projeto

class Coordenacao(models.Model):

    status = models.BooleanField(default=True)
    dt_inicio = models.DateField(null=True, blank=True)
    dt_termino = models.DateField(null=True, blank=True)
    projeto = models.ForeignKey(Projeto, null=True, on_delete=models.CASCADE)
    coordenador = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' % (self.projeto.codigo, self.coordenador.username)