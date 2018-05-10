from django.db import models
from gestaoapp.models.projeto import Projeto
from gestaoapp.models.usuario import Usuario
from gestaoapp.models.horario import Horario

class HoraProjeto(models.Model):
	
	usuario = models.ForeignKey(Usuario)
	projeto = models.ForeignKey(Projeto)
	hora_atribuida = models.ManyToManyField(Horario, blank=True)

	def __unicode__(self):
		return self.usuario