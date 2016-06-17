from django.db import models

class TipoProjeto(models.Model):
	
	tipo = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.tipo