#coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gestaoapp.models import Bolsa
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
            form = FormVinculoBolsa
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
                print("Tacada de sinuca do Ganso")
            else:
                print("Joga a luva goleirão")
                print(form.errors)
            return render(request, self.template, {
                'bolsa': bolsa,
                'form': form
            })
        return render(request, self.template, {})