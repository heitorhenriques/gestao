# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0016_auto_20160608_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='data',
            field=models.CharField(max_length=255, choices=[(b'SEG', b'Segunda-Feira'), (b'TER', b'Terca-Feira'), (b'QUA', b'Quarta-Feira'), (b'QUI', b'Quinta-Feira'), (b'SEX', b'Sexta-Feira')]),
        ),
    ]
