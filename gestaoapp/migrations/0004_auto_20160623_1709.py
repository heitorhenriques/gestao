# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0003_auto_20160623_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucleo',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Pesquisa', b'Pesquisa'), (b'Extensao', b'Extens\xc3\xa3o'), (b'Ensino', b'Ensino'), (b'Pesquisa/Extensao', b'Pesquisa/Extens\xc3\xa3o')]),
        ),
    ]
