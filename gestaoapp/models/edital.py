from django.db import models
from gestaoapp.models.usuario import Usuario
from django.contrib.auth.models import User

class Edital(models.Model):
    numero = models.IntegerField(unique=True)
    orgao_concedente = models.CharField(max_length=255)
    dt_inicio = models.DateField()
    dt_termino = models.DateField()
    url_edital = models.URLField(max_length=200, null=True, blank=True)
    verba = models.FloatField(null=True, blank=True)
    qtd_bolsa = models.IntegerField(null=True, blank=True)
    pdf_edital = models.FileField(null=True, blank=True)
    data_hora_cadastro = models.DateTimeField(auto_now=True)
    responsavel_cadastro = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(str(self.numero))
