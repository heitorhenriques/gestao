from django.db import models

class FaseProjeto(models.Model):
	
	fase = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.fase