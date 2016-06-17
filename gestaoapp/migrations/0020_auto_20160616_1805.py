# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0019_auto_20160616_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='periodo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(1, b'1\xc2\xb0 Semestre'), (2, b'2\xc2\xb0 Semestre'), (3, b'3\xc2\xb0 Semestre'), (4, b'4\xc2\xb0 Semestre'), (5, b'5\xc2\xb0 Semestre'), (6, b'6\xc2\xb0 Semestre'), (7, b'7\xc2\xb0 Semestre'), (8, b'8\xc2\xb0 Semestre'), (9, b'9\xc2\xb0 Semestre'), (10, b'10\xc2\xb0 Semestre')]),
        ),
    ]
