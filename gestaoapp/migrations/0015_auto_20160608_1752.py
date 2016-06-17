# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0014_auto_20160418_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='turno',
            field=models.CharField(max_length=255),
        ),
    ]
