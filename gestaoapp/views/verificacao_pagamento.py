from gestaoapp.models.pagamentos import Pagamentos
from datetime import datetime
from django.core.mail import send_mail


def verifica():

    data = datetime.now()
    mes_antes = data.month - 1
    pagamentos = Pagamentos.objects.all()

    for pagamento in pagamentos:
        if pagamento.dt_pagamento.month == data.month:
            print 'Tudo certo'
        else:
            if pagamento.dt_pagamento.month == mes_antes:
                send_mail(
                    'Teste',
                    'Ola, tudo bem',
                    'orapideks@gmail.com',
                    ['heiitorheenrique@gmail.com'],
                    fail_silently=False,
                )



