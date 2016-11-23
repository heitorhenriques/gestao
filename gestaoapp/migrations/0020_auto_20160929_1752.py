# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0019_auto_20160927_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='situacao',
        ),
        migrations.AddField(
            model_name='projeto',
            name='parceiro',
            field=models.ForeignKey(default=1, to='gestaoapp.Parceiro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='imagem',
            field=models.ImageField(upload_to=b'static/imagens/parceiro', verbose_name=b'Imagem'),
        ),
    ]
