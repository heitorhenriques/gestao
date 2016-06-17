# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0002_auto_20160407_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_fim',
            field=models.TimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.TimeField(unique=True),
        ),
    ]
