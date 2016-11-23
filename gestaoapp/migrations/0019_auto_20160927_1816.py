# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0018_projeto_membros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='membros',
            new_name='membro',
        ),
    ]
