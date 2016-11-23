# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0008_auto_20160919_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='carga_horaria',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
