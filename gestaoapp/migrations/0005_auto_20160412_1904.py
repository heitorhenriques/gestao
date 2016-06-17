# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoapp', '0004_auto_20160407_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('artefato', models.ManyToManyField(to='gestaoapp.Artefato', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=255)),
                ('orgao_concedente', models.CharField(max_length=255)),
                ('verba', models.FloatField()),
                ('qtd_bolsa', models.IntegerField()),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FaseProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fase', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HoraProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_atribuida', models.ManyToManyField(to='gestaoapp.Horario', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=5)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('duracao', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('qtd_bolsa', models.IntegerField()),
                ('data_cadastro', models.DateField(auto_now=True)),
                ('endereco_git', models.URLField()),
                ('atividade', models.ManyToManyField(to='gestaoapp.Atividade')),
                ('coordenador', models.ForeignKey(related_name='coordenador', to='gestaoapp.Usuario')),
                ('edital', models.ManyToManyField(to='gestaoapp.Edital', blank=True)),
                ('equipe', models.ManyToManyField(related_name='bolsistas', to='gestaoapp.Usuario')),
                ('fase', models.ForeignKey(to='gestaoapp.FaseProjeto')),
                ('nucleo', models.ManyToManyField(to='gestaoapp.Nucleo')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SituacaoProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situacao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinculo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo',
            field=models.ForeignKey(to='gestaoapp.TipoRecurso'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='recurso',
            field=models.ManyToManyField(to='gestaoapp.Recurso'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='situacao',
            field=models.ForeignKey(to='gestaoapp.SituacaoProjeto'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.ForeignKey(to='gestaoapp.TipoProjeto'),
        ),
        migrations.AddField(
            model_name='horaprojeto',
            name='projeto',
            field=models.ForeignKey(to='gestaoapp.Projeto'),
        ),
        migrations.AddField(
            model_name='horaprojeto',
            name='usuario',
            field=models.ForeignKey(to='gestaoapp.Usuario'),
        ),
    ]
