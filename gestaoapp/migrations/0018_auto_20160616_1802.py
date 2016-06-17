# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0017_auto_20160608_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='periodo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(1, b'1 Semestre')]),
        ),
    ]
