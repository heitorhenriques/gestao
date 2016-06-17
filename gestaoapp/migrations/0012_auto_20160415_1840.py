# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0011_auto_20160415_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edital',
            name='qtd_bolsa',
        ),
        migrations.RemoveField(
            model_name='edital',
            name='verba',
        ),
        migrations.AddField(
            model_name='projeto',
            name='verba',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
