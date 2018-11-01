from gestaoapp.models.pagamentos import Pagamentos
from datetime import datetime
from django.core.mail import send_mail


def verifica(request):

 data = datetime.now()
 pagamentos = Pagamentos.objects.all()
 mes_antes = data.month -1
 usuarios = []

 for pagamento in pagamentos:
     if pagamento.dt_pagamento.month != data.month:
        if pagamento.dt_pagamento.month == mes_antes:
            usuarios = pagamento.vinculo.usuario
     else:
         print("Esta tudo certo")


 for usuario in usuarios:
     send_mail(
         'Atraso no cadastro de pagamento',
         'Ola, vimos que vc esta atrasado no cadastro de pagamento, por favor entre no nosso site e cadastre o pagamento desse mes',
         'email_da_fabrica@gmail.com',
         [usuario.email],
         fail_silently=False,
     )