# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0012_auto_20160415_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='url_edital',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
