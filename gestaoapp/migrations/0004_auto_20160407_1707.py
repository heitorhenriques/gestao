# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0003_auto_20160407_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_fim',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
