# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from gestaoapp.forms.bolsa import FormBolsa, FormBolsaEdit, FormBolsaPorEdital
from gestaoapp.forms.busca import Busca
from gestaoapp.forms.vinculo import FormVinculoBolsa
from gestaoapp.models import Vinculo, Edital
from gestaoapp.models.bolsa import Bolsa
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroBolsa(LoginRequiredMixin, View):
    template = 'bolsa/cadastro.html'

    def get(self, request, bolsa_id=None, edital_id=None):

        context_dict = {}

        if bolsa_id:
            bolsa = Bolsa.objects.get(id=bolsa_id)
            form = FormBolsaEdit(instance=bolsa)
            editar = True
        else:
            form = FormBolsa()
            editar = False

        if edital_id:
            edital = get_edital(edital_id)
            if edital:
                qtd_bolsa_cadastradas = quantidade_bolsas(edital_id)
                context_dict['edital'] = edital
                context_dict['qtd_bolsa_cadastradas'] = qtd_bolsa_cadastradas
                if qtd_bolsa_cadastradas >= edital.qtd_bolsa:
                    return HttpResponseRedirect(reverse('visualizar_edital', kwargs={'edital_id': edital_id}))

        context_dict['form'] = form
        context_dict['editar'] = editar

        return render(request, self.template, context_dict)

    def post(self, request, bolsa_id=None, edital_id=None):

        context_dict = {}

        if bolsa_id:
            bolsa = Bolsa.objects.get(id=bolsa_id)
            form = FormBolsaEdit(instance=bolsa, data=request.POST)
        else:
            form = FormBolsa(request.POST)

        if edital_id:
            edital = get_edital(edital_id)
            if edital:
                qtd_bolsa_cadastradas = quantidade_bolsas(edital_id)
                context_dict['edital'] = edital
                context_dict['qtd_bolsa_cadastradas'] = qtd_bolsa_cadastradas
                if qtd_bolsa_cadastradas >= edital.qtd_bolsa:
                    return HttpResponseRedirect(reverse('visualizar_edital', kwargs={'edital_id': edital_id}))

        if form.is_valid():
            post = form.save(commit=False)
            post.responsavel_cadastro = User.objects.get(pk=request.user.id)
            post.responsavel_gerencia = Usuario.objects.get(pk=request.user.id)
            post.save()

            msg = "Operação realizada com sucesso!"
            context_dict['msg'] = msg

            form = FormBolsa()

        context_dict['form'] = form
        return render(request, self.template, context_dict)

class ConsultaBolsa(LoginRequiredMixin, View):
    template = 'bolsa/consulta.html'

    def get(self, request):
        form = Busca()
        usuario = Usuario.objects.filter(pk=request.user.id)
        if 1== 1:
            bolsa = Bolsa.objects.all()
            return render(request, self.template,
                          {'bolsas': bolsa, "form": form, "usuario": usuario})
        else:
            bolsa = Bolsa.objects.filter(responsavel_gerencia=request.user.id)
            return render(request, self.template,
                          {'bolsas': bolsa, "form": form, "usuario": usuario})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            bolsa = Bolsa.objects.filter(nome__icontains=form.cleaned_data['codigo'])

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
            vinculos = Vinculo.objects.filter(bolsa=bolsa).order_by('-dt_inicio')
        else:
            return render(request, self.template, {})

        return render(request, self.template, {'bolsa': bolsa, 'vinculos': vinculos})

    def post(self, request):

        return render(request, self.template)


def get_edital(edital_id):
    try:
        return Edital.objects.get(pk=edital_id)
    except:
        return None


def quantidade_bolsas(edital_id):
    return Bolsa.objects.filter(edital=edital_id).count()


