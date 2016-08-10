# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0004_auto_20160623_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.IntegerField(max_length=255),
        ),
    ]
