# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0005_auto_20160808_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
