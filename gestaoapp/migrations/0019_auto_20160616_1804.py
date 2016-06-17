# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0018_auto_20160616_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='periodo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(1, b'1\xc2\xb0 Semestre')]),
        ),
    ]
