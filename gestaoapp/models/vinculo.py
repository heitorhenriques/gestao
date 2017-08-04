# coding:utf-8
from django.db import models

from gestaoapp.models.bolsa import Bolsa
from gestaoapp.models.usuario import Usuario


class Vinculo(models.Model):

    status = models.BooleanField(default=True)
    dt_inicio = models.DateField(null=True, blank=True)
    dt_termino = models.DateField(null=True, blank=True)
    bolsa = models.ForeignKey(Bolsa, null=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s' %(self.bolsa.codigo, self.usuario.username)