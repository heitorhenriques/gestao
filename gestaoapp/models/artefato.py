from django.db import models

class Artefato(models.Model):
	
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length = 255)

	def __unicode__(self):
		return self.nome