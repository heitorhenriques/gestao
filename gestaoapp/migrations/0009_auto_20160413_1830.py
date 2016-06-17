# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0008_auto_20160413_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='fase',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='situacao',
        ),
    ]
