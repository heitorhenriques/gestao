# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0005_auto_20160412_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='atividade',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='endereco_git',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='equipe',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='recurso',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(blank=True, to='gestaoapp.SituacaoProjeto', null=True),
        ),
    ]
