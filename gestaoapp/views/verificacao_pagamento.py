from gestaoapp.models.pagamentos import Pagamentos
from datetime import datetime


data = datetime.now()
pagamentos = Pagamentos.objects.all()
prox_mes = data.month + 1
usuarios = []
dias_atrasos = []


for pagamento in pagamentos:
    if pagamento.dt_pagamento.month == prox_mes:
        msg = 'Tudo certo'
    else:
        dias_atrasos = data.day
        usuarios = pagamento.vinculo.usuario


for dia_atrasos,usuario in dias_atrasos,usuarios:

    print ('Usuario % esta % dias atrasado' % (dia_atrasos, usuario))
