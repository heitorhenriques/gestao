# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0006_auto_20160412_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='fase',
            field=models.ForeignKey(blank=True, to='gestaoapp.FaseProjeto', null=True),
        ),
    ]
