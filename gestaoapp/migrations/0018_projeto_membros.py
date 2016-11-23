# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0017_parceiro_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(related_name='Membros', to='gestaoapp.Usuario', blank=True),
        ),
    ]
