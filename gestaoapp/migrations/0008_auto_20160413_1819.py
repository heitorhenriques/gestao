# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0007_auto_20160413_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='fase',
            field=models.ForeignKey(to='gestaoapp.FaseProjeto', null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(to='gestaoapp.SituacaoProjeto', null=True),
        ),
    ]
