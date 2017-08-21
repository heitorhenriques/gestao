from django.db import models
from gestaoapp.models.usuario import User


class Curso(models.Model):
    curso = models.CharField(max_length=255)
    data_hora_cadastro = models.DateTimeField(auto_now=True)
    responsavel_cadastro = models.ForeignKey(User)

    def __unicode__(self):
        return self.curso
