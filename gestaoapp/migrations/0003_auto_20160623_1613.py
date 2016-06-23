# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0002_auto_20160617_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='periodo',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'primeiro', b'1\xc2\xb0 Semestre'), (b'segundo', b'2\xc2\xb0 Semestre'), (b'terceiro', b'3\xc2\xb0 Semestre'), (b'quarto', b'4\xc2\xb0 Semestre'), (b'quinto', b'5\xc2\xb0 Semestre'), (b'sexto', b'6\xc2\xb0 Semestre'), (b'setimo', b'7\xc2\xb0 Semestre'), (b'oitavo', b'8\xc2\xb0 Semestre'), (b'nono', b'9\xc2\xb0 Semestre'), (b'decimo', b'10\xc2\xb0 Semestre')]),
        ),
    ]
