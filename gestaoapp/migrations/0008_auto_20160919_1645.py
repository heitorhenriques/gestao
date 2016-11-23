# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0007_auto_20160919_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='lattes',
            field=models.URLField(null=True, blank=True),
        ),
    ]
