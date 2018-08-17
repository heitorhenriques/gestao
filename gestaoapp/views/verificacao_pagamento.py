from gestaoapp.models.pagamentos import Pagamentos
from datetime import datetime


def verifica():

    data = datetime.now()
    mes_antes = data.month - 1
    pagamentos = Pagamentos.objects.all()

    for pagamento in pagamentos:
        if pagamento.dt_pagamento.month == data.month:
            print 'Tudo certo'
        else:
            if pagamento.dt_pagamento.month == mes_antes:
                print ('Usuario %s esta atrasado' % pagamento.vinculo.usuario.first_name)