from django.db import models

class SituacaoProjeto(models.Model):
	
	situacao = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.situacao