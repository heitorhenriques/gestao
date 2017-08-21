from django.db import models
# from gestaoapp.models.usuario import Usuario
from django.contrib.auth.models import User

class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    imagem = models.ImageField("Imagem", upload_to='parceiro')
    site = models.URLField(max_length=200, blank=True, null=True)
    data_hora_cadastro = models.DateTimeField(auto_now=True)
    responsavel_cadastro = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome
