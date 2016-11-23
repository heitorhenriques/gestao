# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0009_auto_20160919_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='vinculo_institucional',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Aluno', b'Aluno'), (b'Professor', b'Professor'), (b'Colaborador', b'Colaborador')]),
        ),
    ]
