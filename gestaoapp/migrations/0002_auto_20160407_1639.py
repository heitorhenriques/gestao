# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='horario',
            name='turno',
            field=models.ForeignKey(to='gestaoapp.Turno'),
        ),
    ]
