#coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gestaoapp.models import Bolsa
from gestaoapp.models import Vinculo
from gestaoapp.views.loginrequired import LoginRequiredMixin

from gestaoapp.forms.vinculo import FormVinculo, FormVinculoBolsa

class CadastroVinculo(LoginRequiredMixin, View):

    template = 'vinculo/cadastro.html'

    def get(self, request):
        form = FormVinculo()
        return render(request, self.template, {
            'form': form
        })

    def post(self, request):
        form = FormVinculo(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {
            'form': form
        })

class CadastroVinculoBolsa(LoginRequiredMixin, View):

    template = 'vinculo/vincular_bolsa.html'

    def get(self, request, bolsa_id=None):
        if bolsa_id:
            bolsa = Bolsa.objects.get(pk=bolsa_id)
            form = FormVinculoBolsa(bolsa=bolsa)

            return render(request, self.template, {
                'bolsa': bolsa,
                'form': form
            })
        return render(request, self.template, {})

    def post(self, request, bolsa_id=None):

        if bolsa_id:
            bolsa = Bolsa.objects.get(pk=bolsa_id)
            form = FormVinculoBolsa(data=request.POST)

            if form.is_valid():
                vinculo = form.save(commit=False)
                vinculo.bolsa = bolsa
                self.desativar_vinculos_atuais(dt_termino=vinculo.dt_inicio, bolsa=bolsa)
                vinculo.save()
                msg = {'status': True, 'texto': 'Vínculo registrado com sucesso!'}
            else:
                msg = {'status': False, 'texto': 'Não foi possível registrar o novo vínculo!'}
            return render(request, self.template, {
                'bolsa': bolsa,
                'form': form,
                'msg': msg
            })
        return render(request, self.template, {})

    def desativar_vinculos_atuais(self, dt_termino, bolsa):
        vinculos_ativos = Vinculo.objects.filter(status=True, bolsa=bolsa)
        for v in vinculos_ativos:
            v.status = False
            if not v.dt_termino:
                v.dt_termino = dt_termino
            v.save()