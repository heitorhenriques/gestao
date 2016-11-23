# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0016_auto_20160922_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiro',
            name='site',
            field=models.URLField(null=True, blank=True),
        ),
    ]
