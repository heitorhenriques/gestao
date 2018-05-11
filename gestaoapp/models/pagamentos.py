from django.db import models

class Pagamentos(models.Model):

    dt_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.dt_pagamento