# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0009_auto_20160413_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(to='gestaoapp.SituacaoProjeto', null=True),
        ),
    ]
