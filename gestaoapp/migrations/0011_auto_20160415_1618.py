# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0010_projeto_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(blank=True, to='gestaoapp.SituacaoProjeto', null=True),
        ),
    ]
