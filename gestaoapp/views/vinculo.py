#coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.views.loginrequired import LoginRequiredMixin

from gestaoapp.forms.vinculo import FormVinculo

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
