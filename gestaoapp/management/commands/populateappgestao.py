import datetime

from django.core.management.base import BaseCommand
from gestaoapp.models.pagamentos import Pagamentos
from gestaoapp.models.bolsa import Bolsa
from gestaoapp.models.vinculo import Vinculo
from gestaoapp.models.edital import Edital
from gestaoapp.models.usuario import Usuario
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_gestao(self):

        usuario, created = Usuario.objects.get_or_create(
            vinculo_institucional= u'Aluno',
            matricula= u'12345',
            foto= u'jvnsnv',
            carga_horaria= u'25',
            telefone1= u'8488939',
            desc= u'bnvbsiaej',
            first_name= u'Fred',
            last_name= u'Silva',
            username= u'Fred',
            email= u'fred@a.com'
        )
        usuario.set_password(u'Fred')
        usuario.save()

        usuario1, created = Usuario.objects.get_or_create(
            vinculo_institucional=u'Professor',
            matricula=u'94898',
            foto=u'jvnsnv',
            carga_horaria=u'98',
            telefone1=u'3727284',
            desc=u'bnvbsiaej',
            first_name=u'Heitor',
            last_name=u'Silva',
            username=u'Heitor',
            email=u'heitor@a.com'
        )
        usuario1.is_superuser = '1'
        usuario1.set_password(u'Heitor')
        usuario1.save()

        usuario2, created = Usuario.objects.get_or_create(
            vinculo_institucional=u'Professor',
            matricula=u'88979',
            foto=u'jvnsnv',
            carga_horaria=u'98',
            telefone1=u'3727284',
            desc=u'bnvbsiaej',
            first_name=u'Nicholas',
            last_name=u'Silva',
            username=u'nicholas',
            email=u'heitor@a.com'
        )
        usuario2.is_superuser = '1'
        usuario2.set_password(u'nicholas')
        usuario2.save()

        edital, created = Edital.objects.get_or_create(
            numero= u'451521',
            orgao_concedente= u'jnfaufai',
            dt_inicio= datetime.date.today(),
            dt_termino= datetime.date.today(),
            responsavel_cadastro= usuario
        )
        edital.save()

        bolsa, created = Bolsa.objects.get_or_create(
            codigo=u'46236',
            valor=u'400.00',
            dt_inicio=datetime.date.today(),
            dt_termino=datetime.date.today(),
            edital= edital,
            status=u'True',
            responsavel_cadastro_id= u'1',
            responsavel_gerencia_id= u'1',
        )
        bolsa.save()

        bolsa, created = Bolsa.objects.get_or_create(
            codigo=u'36626',
            valor=u'200.00',
            dt_inicio=datetime.date.today(),
            dt_termino=datetime.date.today(),
            edital= edital,
            status=u'True',
            responsavel_cadastro_id=u'2',
            responsavel_gerencia_id=u'2',
        )
        bolsa.save()

        vinculo, created = Vinculo.objects.get_or_create(
            status = u'True',
            dt_inicio = datetime.date.today(),
            dt_termino = datetime.date.today(),
            bolsa = bolsa,
            usuario= usuario1,
        )
        vinculo.save()

        vinculo, created = Vinculo.objects.get_or_create(
            status=u'True',
            dt_inicio=datetime.date.today(),
            dt_termino=datetime.date.today(),
            bolsa=bolsa,
            usuario= usuario,
        )
        vinculo.save()

        pagamento, created = Pagamentos.objects.get_or_create(
            dt_pagamento = datetime.date.today(),
            vinculo = vinculo,
            valor = u'200.00',
        )
        pagamento.save()

    def handle(self, *args, **options):
        self._create_gestao()
