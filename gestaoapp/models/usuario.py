# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from gestaoapp.models.horario import Horario
from PIL import Image

class Usuario(User):
	
	PERIODO_CHOICES = (
		(1, '1° Semestre'),
		(2, '2° Semestre'),
		(3, '3° Semestre'),
		(4, '4° Semestre'),
		(5, '5° Semestre'),
		(6, '6° Semestre'),
		(7, '7° Semestre'),
		(8, '8° Semestre'),
		(9, '9° Semestre'),
		(10, '10° Semestre'),
		
	)
	periodo = models.CharField(
		max_length=255,null=True, blank=True,
		choices=PERIODO_CHOICES
	)

	email_opcional = models.EmailField(max_length=254, null=True, blank=True)
	matricula = models.CharField(max_length=255, unique = True)
	foto = models.ImageField('Imagem', upload_to='imagens')
	carga_horaria = models.IntegerField()
	telefone1 = models.CharField(max_length=11)
	telefone2 = models.CharField(max_length=11, blank=True, null=True)
	vinculo_institucional = models.CharField(max_length=255,null=True, blank=True)
	curso = models.CharField(max_length=255, null=True, blank=True)
	dia = models.ManyToManyField(Horario, blank=True)
	verificacao=models.CharField(max_length=255,null=True, blank=True, unique = True)

	def __unicode__(self):
		return self.first_name