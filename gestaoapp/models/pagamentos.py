# -*- coding: utf-8 -*-

from django.db import models
from gestaoapp.models.vinculo import Vinculo


class Pagamentos(models.Model):
    dt_pagamento = models.DateField(null=True, blank=True)
    vinculo = models.ForeignKey(Vinculo)
    valor = models.FloatField(null=True)

    def __str__(self):
        return ('%s %s %s' % (self.dt_pagamento, self.vinculo, self.vinculo.bolsa))


