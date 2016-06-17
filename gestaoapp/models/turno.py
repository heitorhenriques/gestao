from django.db import models

class Turno(models.Model):
	
	turno = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.turno