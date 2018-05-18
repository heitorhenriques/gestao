# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from gestaoapp.views.loginrequired import LoginRequiredMixin
from gestaoapp.models.pagamentos import Pagamentos
from gestaoapp.forms.pagamento import FormPagamento


class CadastroPagamento(LoginRequiredMixin,View):
    template = 'pagamentos/cadastro.html'

    def get(self,request,pagamento_id=None):

        context_dict = {}

        if pagamento_id:
            pagamento = Pagamentos.objects.get(id=pagamento_id)
            form = FormPagamento(instance=pagamento)
            editar = True

        else:
            form = FormPagamento()
            editar = False


        context_dict['form'] = form
        context_dict['editar'] = editar

        return render(request, self.template, context_dict)

    def post(self,request,pagamento_id=None):
        context_dict = {}

        if pagamento_id:
            pagamento = Pagamentos.objects.get(id=pagamento_id)
            form = FormPagamento(instance=pagamento, data=request.POST)

        else:
            form = FormPagamento(request.POST)


        if form.is_valid():
            form.save()
            msg = 'Operação realizada com sucesso'

            context_dict['msg'] = msg
            form = FormPagamento()

        context_dict['form'] = form

        return render(request,self.template,context_dict)


class ConsultaPagamento(LoginRequiredMixin, View):
    template = 'pagamentos/consulta.html'

    def get(self,request):
        pagamentos = Pagamentos.objects.all()

        return render(request, self.template, {'pagamentos': pagamentos})
