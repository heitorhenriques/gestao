from django.db import models

from gestaoapp.models.usuario import Usuario


class Horario(models.Model):
    MANHA = 'MA'
    TARDE = 'TA'
    NOITE = 'NO'

    HORARIO_CHOICES = (
        (MANHA, 'Manha'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    )

    turno = models.CharField(
        max_length=2,
        choices=HORARIO_CHOICES
    )

    SEGUNDA = 'SEG'
    TERCA = 'TER'
    QUARTA = 'QUA'
    QUINTA = 'QUI'
    SEXTA = 'SEX'

    DIA_CHOICES = (
        (SEGUNDA, 'Segunda-Feira'),
        (TERCA, 'Terca-Feira'),
        (QUARTA, 'Quarta-Feira'),
        (QUINTA, 'Quinta-Feira'),
        (SEXTA, 'Sexta-Feira'),
    )
    data = models.CharField(
        max_length=255,
        choices=DIA_CHOICES
    )

    usuario = models.ForeignKey(Usuario, null=False, blank=False)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

