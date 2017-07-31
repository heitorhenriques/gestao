# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View

from gestaoapp.forms.bolsa import FormBolsa, FormBolsaEdit
from gestaoapp.forms.busca import Busca
from gestaoapp.models.bolsa import Bolsa
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroBolsa(LoginRequiredMixin, View):
    template = 'bolsa/cadastro.html'

    def get(self, request, bolsa_id=None):

        if bolsa_id:
            bolsa = Bolsa.objects.get(id=bolsa_id)
            form = FormBolsaEdit(instance=bolsa)
            editar = True
        else:
            form = FormBolsa()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar})

    def post(self, request, bolsa_id=None):

        if bolsa_id:
            bolsa = Bolsa.objects.get(id=bolsa_id)
            form = FormBolsaEdit(instance=bolsa, data=request.POST)
        else:
            form = FormBolsa(request.POST)

        if form.is_valid():
            form.save(request)
            msg = "Operação realizada com sucesso!"

            form = FormBolsa()

            return render(request, self.template, {'form': form, 'msg': msg})
            # return redirect('/cadastro_sucesso')

        else:
            return render(request, self.template, {'form': form})


class ConsultaBolsa(LoginRequiredMixin, View):
    template = 'bolsa/consulta.html'

    def get(self, request):
        form = Busca()
        bolsa = Bolsa.objects.all()

        return render(request, self.template, {'bolsas': bolsa, "form": form})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            bolsa = Bolsa.objects.filter(nome__icontains=form.cleaned_data['numero'])

            return render(request, self.template, {'bolsas': bolsa, 'form': form})
        else:
            form = Busca(request.POST)
            bolsa = Bolsa.objects.all()
        return render(request, self.template, {'bolsas': bolsa, "form": form})


class VisualizarBolsa(LoginRequiredMixin, View):
    template = "bolsa/visualizar.html"

    def get(self, request, bolsa_id=None):

        if bolsa_id:
            bolsa = Bolsa.objects.get(id=bolsa_id)

        else:
            return render(request, self.template, {})

        return render(request, self.template, {'bolsa': bolsa})

    def post(self, request):

        return render(request, self.template)
