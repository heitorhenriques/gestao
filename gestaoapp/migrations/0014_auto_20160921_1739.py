# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0013_parceiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiro',
            name='descricao',
            field=models.TextField(),
        ),
    ]
