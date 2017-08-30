# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

from gestaoapp.models.edital import Edital
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.models.parceiro import Parceiro
from gestaoapp.models.usuario import Usuario


class Projeto(models.Model):
    TIPO_CHOICES = (
        ('Pesquisa', 'Pesquisa'),
        ('Extensao', 'Extensão'),
        ('Ensino', 'Ensino'),
        ('Pesquisa_Extensao', 'Pesquisa/Extensão'),

    )
    tipo = models.CharField(
        max_length=255, null=True, blank=True,
        choices=TIPO_CHOICES
    )

    nome = models.CharField(max_length=255)
    imagem = models.ImageField("Imagem", upload_to='projeto')
    codigo = models.CharField(max_length=255, unique=True)
    # tipo = models.ForeignKey(TipoProjeto)
    data_hora_cadastro = models.DateTimeField(auto_now=True)
    responsavel_cadastro = models.ForeignKey(User, related_name= "coordenador_criador", )
    # coordenador = models.ForeignKey(Usuario, related_name="coordenador")
    coordenador = models.ManyToManyField(Usuario, through='Coordenacao', blank=True)
    duracao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nucleo = models.ManyToManyField(Nucleo)
    edital = models.ManyToManyField(Edital, blank=True, related_name="editais_do_projeto")
    descricao = models.TextField()
    # data_cadastro = models.DateField(auto_now=True)
    # situacao = models.ForeignKey(SituacaoProjeto, null=True, blank=True)
    membro = models.ManyToManyField(Usuario, blank=True, related_name="membros")
    parceiro = models.ManyToManyField(Parceiro, blank=True)

    def __unicode__(self):
        return self.nome
