from django.db import models

class Edital (models.Model):
	numero = models.IntegerField()
	orgao_concedente = models.CharField(max_length =255)
	dt_inicio = models.DateField()
	dt_termino = models.DateField()
	url_edital = models.URLField(max_length=200)
	verba = models.FloatField()
	qtd_bolsa = models.IntegerField()

	def __unicode__(self):
		return self.numero