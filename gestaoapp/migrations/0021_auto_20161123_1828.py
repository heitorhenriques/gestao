# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0020_auto_20160929_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiro',
            name='imagem',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='parceiro',
        ),
        migrations.AddField(
            model_name='projeto',
            name='parceiro',
            field=models.ManyToManyField(to='gestaoapp.Parceiro'),
        ),
    ]
