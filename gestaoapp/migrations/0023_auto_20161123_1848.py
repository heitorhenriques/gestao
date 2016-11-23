# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0022_auto_20161123_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiro',
            name='imagem',
            field=models.ImageField(upload_to=b'/static/imagens/parceiro/', verbose_name=b'Imagem'),
        ),
    ]
