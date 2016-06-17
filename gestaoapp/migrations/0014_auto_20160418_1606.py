# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0013_edital_url_edital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='qtd_bolsa',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='verba',
        ),
        migrations.AddField(
            model_name='edital',
            name='qtd_bolsa',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edital',
            name='verba',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
