# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Bolsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=255)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
                ('qtd_pagamento', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coordenacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_inicio', models.DateField(null=True, auto_created=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('dt_termino', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso', models.CharField(max_length=255)),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(unique=True)),
                ('orgao_concedente', models.CharField(max_length=255)),
                ('dt_inicio', models.DateField()),
                ('dt_termino', models.DateField()),
                ('url_edital', models.URLField(null=True, blank=True)),
                ('verba', models.FloatField(null=True, blank=True)),
                ('qtd_bolsa', models.IntegerField(null=True, blank=True)),
                ('pdf_edital', models.FileField(null=True, upload_to=b'', blank=True)),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
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
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=2, choices=[(b'MA', b'Manha'), (b'TA', b'Tarde'), (b'NO', b'Noite')])),
                ('data', models.CharField(max_length=255, choices=[(b'SEG', b'Segunda-Feira'), (b'TER', b'Terca-Feira'), (b'QUA', b'Quarta-Feira'), (b'QUI', b'Quinta-Feira'), (b'SEX', b'Sexta-Feira')])),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=5)),
                ('descricao', models.TextField()),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt_pagamento', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('endereco', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to=b'parceiro', verbose_name=b'Imagem')),
                ('site', models.URLField(null=True, blank=True)),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Pesquisa', b'Pesquisa'), (b'Extensao', b'Extens\xc3\xa3o'), (b'Ensino', b'Ensino'), (b'Pesquisa_Extensao', b'Pesquisa/Extens\xc3\xa3o')])),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to=b'projeto', verbose_name=b'Imagem')),
                ('codigo', models.CharField(unique=True, max_length=255)),
                ('data_hora_cadastro', models.DateTimeField(auto_now=True)),
                ('duracao', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('descricao', models.TextField()),
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
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('periodo', models.CharField(blank=True, max_length=255, null=True, choices=[(b'primeiro', b'1\xc2\xb0 Semestre'), (b'segundo', b'2\xc2\xb0 Semestre'), (b'terceiro', b'3\xc2\xb0 Semestre'), (b'quarto', b'4\xc2\xb0 Semestre'), (b'quinto', b'5\xc2\xb0 Semestre'), (b'sexto', b'6\xc2\xb0 Semestre'), (b'setimo', b'7\xc2\xb0 Semestre'), (b'oitavo', b'8\xc2\xb0 Semestre'), (b'nono', b'9\xc2\xb0 Semestre'), (b'decimo', b'10\xc2\xb0 Semestre')])),
                ('vinculo_institucional', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Aluno', b'Aluno'), (b'Professor', b'Professor')])),
                ('email_opcional', models.EmailField(max_length=254, null=True, blank=True)),
                ('matricula', models.CharField(unique=True, max_length=255)),
                ('foto', models.ImageField(upload_to=b'profile_images')),
                ('carga_horaria', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('telefone1', models.CharField(max_length=11)),
                ('telefone2', models.CharField(max_length=11, null=True, blank=True)),
                ('verificacao', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('lattes', models.URLField(null=True, blank=True)),
                ('desc', models.TextField()),
                ('super_adm', models.BooleanField(default=False)),
                ('curso', models.ForeignKey(blank=True, to='gestaoapp.Curso', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('dt_inicio', models.DateField(null=True, blank=True)),
                ('dt_termino', models.DateField(null=True, blank=True)),
                ('bolsa', models.ForeignKey(to='gestaoapp.Bolsa', null=True)),
                ('usuario', models.ForeignKey(to='gestaoapp.Usuario', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo',
            field=models.ForeignKey(to='gestaoapp.TipoRecurso'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='coordenador',
            field=models.ManyToManyField(to='gestaoapp.Usuario', through='gestaoapp.Coordenacao', blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='edital',
            field=models.ManyToManyField(related_name='editais_do_projeto', to='gestaoapp.Edital', blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='membro',
            field=models.ManyToManyField(related_name='membros', to='gestaoapp.Usuario', blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='nucleo',
            field=models.ManyToManyField(to='gestaoapp.Nucleo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='parceiro',
            field=models.ManyToManyField(to='gestaoapp.Parceiro', blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='responsavel_cadastro',
            field=models.ForeignKey(related_name='coordenador_criador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='parceiro',
            name='responsavel_cadastro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagamentos',
            name='vinculo',
            field=models.ForeignKey(to='gestaoapp.Vinculo'),
        ),
        migrations.AddField(
            model_name='nucleo',
            name='responsavel_cadastro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='horario',
            name='usuario',
            field=models.ForeignKey(to='gestaoapp.Usuario'),
        ),
        migrations.AddField(
            model_name='edital',
            name='responsavel_cadastro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='responsavel_cadastro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='coordenador',
            field=models.ForeignKey(to='gestaoapp.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='projeto',
            field=models.ForeignKey(to='gestaoapp.Projeto', null=True),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='edital',
            field=models.ForeignKey(to='gestaoapp.Edital'),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='responsavel_cadastro',
            field=models.ForeignKey(related_name='responsavel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='responsavel_gerencia',
            field=models.ForeignKey(related_name='responsavel_gerencia', to='gestaoapp.Usuario'),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='vinculos',
            field=models.ManyToManyField(to='gestaoapp.Usuario', through='gestaoapp.Vinculo', blank=True),
        ),
    ]
