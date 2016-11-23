# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0012_auto_20160919_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to=b'gestao/imagens/parceiro', verbose_name=b'Imagem')),
            ],
        ),
    ]
