from django.db import models

class Vinculo(models.Model):
	
	vinculo = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.vinculo