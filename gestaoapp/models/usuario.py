# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from gestaoapp.models.horario import Horario
from gestaoapp.models.curso import Curso
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator

class Usuario(User):
	
	PERIODO_CHOICES = (
		('primeiro', '1° Semestre'),
		('segundo', '2° Semestre'),
		('terceiro', '3° Semestre'),
		('quarto', '4° Semestre'),
		('quinto', '5° Semestre'),
		('sexto', '6° Semestre'),
		('setimo', '7° Semestre'),
		('oitavo', '8° Semestre'),
		('nono', '9° Semestre'),
		('decimo', '10° Semestre'),
	)

	VINCULO_CHOICES = (
		('Aluno', 'Aluno'),
		('Professor', 'Professor'),
		#('Colaborador', 'Colaborador'),
	)

	periodo = models.CharField(
		max_length=255,null=True, blank=True,
		choices=PERIODO_CHOICES
	)
	vinculo_institucional = models.CharField(
		max_length=255,null=True, blank=True, 
		choices=VINCULO_CHOICES)

	email_opcional = models.EmailField(max_length=254, null=True, blank=True)
	matricula = models.CharField(max_length=255, unique = True)
	foto = models.ImageField('Imagem', upload_to='static/imagens/')
	carga_horaria = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
	telefone1 = models.CharField(max_length=11)
	telefone2 = models.CharField(max_length=11, blank=True, null=True)
	curso = models.ForeignKey(Curso, null=True, blank=True)
	dia = models.ManyToManyField(Horario, blank=True)
	verificacao=models.CharField(max_length=255,null=True, blank=True, unique = True)
	lattes = models.URLField(null=True, blank=True)
	desc = models.TextField()

	def __unicode__(self):
		return self.first_name