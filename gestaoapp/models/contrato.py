from django.db import models
from gestaoapp.models.turno import Usuario

class Contrato(models.Model):
	
	aluno = models.ManyToManyField(Usuario)
	edital = models.ManyToManyField(Usuario)
	desc = models.CharField(max_length = 255)

	def __unicode__(self):
		return self.nome