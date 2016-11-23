from django.db import models

class Parceiro(models.Model):
	
	nome = models.CharField(max_length=255)
	cnpj = models.CharField(max_length=255)
	descricao = models.TextField()
	endereco = models.CharField(max_length = 255)
	imagem = models.ImageField('Imagem', upload_to='static/imagens/parceiro')
	site = models.URLField(max_length=200, blank = True, null = True)

	def __unicode__(self):
		return self.nome