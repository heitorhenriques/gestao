# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0015_auto_20160608_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='turno',
            field=models.CharField(max_length=2, choices=[(b'MA', b'Manha'), (b'TA', b'Tarde'), (b'NO', b'Noite')]),
        ),
    ]
