from django.db import models
from gestaoapp.models.artefato import Artefato

class Atividade(models.Model):
	
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length = 255)
	artefato = models.ManyToManyField(Artefato, blank = True)

	def __unicode__(self):
		return self.nome