# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0011_auto_20160919_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='codigo',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
