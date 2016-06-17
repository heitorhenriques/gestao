# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0020_auto_20160616_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Pesquisa', b'Pesquisa')]),
        ),
    ]
