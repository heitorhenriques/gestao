# -*- coding: utf-8 -*-

from django.db import models
from gestaoapp.models.vinculo import Vinculo

class Pagamentos(models.Model):

    dt_pagamento = models.DateField(null=True, blank=True)
    vinculo = models.ForeignKey(Vinculo)

    def __str__(self):
        return self.dt_pagamento