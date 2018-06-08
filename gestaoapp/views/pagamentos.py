# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from gestaoapp.views.loginrequired import LoginRequiredMixin
from gestaoapp.models.pagamentos import Pagamentos
from gestaoapp.forms.pagamento import FormPagamento
from gestaoapp.models.vinculo import Vinculo
from gestaoapp.models.usuario import Usuario


class CadastroPagamento(LoginRequiredMixin, View):
    template = 'pagamentos/cadastro.html'

    def get(self, request, pagamento_id=None):

        context_dict = {}
        usuario = Usuario.objects.get(id=request.user.id)
        vinculo = Vinculo.objects.get(usuario=usuario)
        if pagamento_id:
            pagamento = Pagamentos.objects.get(id=pagamento_id)
            form = FormPagamento(instance=pagamento)
            editar = True

        else:
            form = FormPagamento()
            editar = False

        context_dict['form'] = form
        context_dict['editar'] = editar
        context_dict['vinculo'] = vinculo

        return render(request, self.template, context_dict)

    def post(self, request, pagamento_id=None):
        context_dict = {}

        if pagamento_id:
            pagamento = Pagamentos.objects.get(id=pagamento_id)
            form = FormPagamento(instance=pagamento)

        else:
            form = FormPagamento(request.POST)

        if form.is_valid(): #TODO form deu errado
            form.save()
            msg = 'Operação realizada com sucesso'

            context_dict['msg'] = msg
            form = FormPagamento()

        context_dict['form'] = form

        return render(request, self.template, context_dict)


class ConsultaPagamento(LoginRequiredMixin, View):
    template = 'pagamentos/consulta.html'

    def get(self, request):
        context_dict = {}
        usuario = Usuario.objects.get(id=request.user.id)
        vinculo = Vinculo.objects.filter(usuario=usuario)
        if usuario.super_adm == 1:
            context_dict['pagamentos'] = Pagamentos.objects.all()

        else:
            if vinculo:
                context_dict['pagamentos'] = Pagamentos.objects.filter(vinculo=vinculo)

        return render(request, self.template, context_dict)


def get_vinculo(vinculo_id):
    try:
        return Vinculo.objects.get(pk=vinculo_id)
    except:
        return None
