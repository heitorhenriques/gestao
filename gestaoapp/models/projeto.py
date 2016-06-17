# encoding: utf-8
from django.db import models
from gestaoapp.models.recurso import Recurso
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.models.usuario import Usuario
from gestaoapp.models.atividade import Atividade
from gestaoapp.models.edital import Edital
from gestaoapp.models.tipoprojeto import TipoProjeto
from gestaoapp.models.situacaoprojeto import SituacaoProjeto
from gestaoapp.models.faseprojeto import FaseProjeto

class Projeto(models.Model):
	
	TIPO_CHOICES = (
		('Pesquisa', 'Pesquisa'),
		('Extensão', 'Extensão'),
		('Ensino', 'Ensino'),
		('Pesquisa/Extensão', 'Pesquisa/Extensão'),
		
	)
	tipo = models.CharField(
		max_length=255,null=True, blank=True,
		choices=TIPO_CHOICES
	)

	
	nome = models.CharField(max_length = 255)
	codigo = models.CharField(max_length= 255)
	#tipo = models.ForeignKey(TipoProjeto)
	coordenador = models.ForeignKey(Usuario,related_name = "coordenador")
	duracao = models.CharField(max_length = 255)
	data_inicio = models.DateField()
	data_fim = models.DateField()
	nucleo = models.ManyToManyField(Nucleo)
	edital = models.ManyToManyField(Edital, blank=True)
	descricao = models.TextField()
	data_cadastro =  models.DateField(auto_now= True)
	situacao = models.ForeignKey(SituacaoProjeto, null=True, blank=True)
	

	def __unicode__(self):
		return self.nome