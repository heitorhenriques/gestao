# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0021_auto_20160616_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Pesquisa', b'Pesquisa'), (b'Extens\xc3\xa3o', b'Extens\xc3\xa3o'), (b'Ensino', b'Ensino'), (b'Pesquisa/Extens\xc3\xa3o', b'Pesquisa/Extens\xc3\xa3o')]),
        ),
    ]
