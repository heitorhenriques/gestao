from django.db import models

class Curso(models.Model):
	
	curso = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.curso