from django.db import models
from datetime import datetime

from gestaoapp.models.edital import Edital
from gestaoapp.models.usuario import Usuario

#from gestaoapp.models.vinculo import Vinculo


class Bolsa(models.Model):

    codigo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    dt_inicio = models.DateField()
    dt_termino = models.DateField()
    edital = models.ForeignKey(Edital)
    qtd_pagamento = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=True)
    vinculos = models.ManyToManyField(Usuario, through='Vinculo', blank=True)

    def save(self, *args, **kwargs):
        meses = ((self.dt_termino - self.dt_inicio).days) / 30
        self.qtd_pagamento = meses
        super(Bolsa, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.codigo
