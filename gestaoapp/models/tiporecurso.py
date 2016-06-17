from django.db import models

class TipoRecurso(models.Model):
	
	tipo = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.tipo