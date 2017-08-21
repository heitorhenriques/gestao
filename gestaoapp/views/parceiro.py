# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User

from gestaoapp.forms.busca import Busca
from gestaoapp.forms.parceiro import FormParceiro, FormParceiroEdit
from gestaoapp.models.parceiro import Parceiro
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroParceiro(LoginRequiredMixin, View):
    template = 'parceiro/cadastro.html'

    def get(self, request, parceiro_id=None):

        if parceiro_id:
            nome = Parceiro.objects.get(id=parceiro_id)
            form = FormParceiroEdit(instance=nome)
            editar = True
        else:
            form = FormParceiro()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar})

    def post(self, request, parceiro_id=None):

        if parceiro_id:
            nome = Parceiro.objects.get(id=parceiro_id)
            form = FormParceiroEdit(instance=nome, data=request.POST)
        else:
            form = FormParceiro(request.POST, request.FILES)

        if form.is_valid():
            # form.save(request)

            post = form.save(commit=False)
            post.responsavel_cadastro = User.objects.get(pk=request.user.id)
            post.save()

            user = form.save(commit=False)
            if 'imagem' in request.FILES:
                user.imagem = request.FILES['imagem']
            user.save()

            msg = "Operação realizada com sucesso!"
            form = FormParceiro()

            # return redirect('/cadastro_sucesso')
            return render(request, self.template, {'form': form, 'msg': msg})
        else:
            return render(request, self.template, {'form': form})


class ConsultaParceiro(LoginRequiredMixin, View):
    template = 'parceiro/consulta.html'

    def get(self, request):
        form = Busca()
        parceiro = Parceiro.objects.all()

        return render(request, self.template, {'parceiros': parceiro, "form": form})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            parceiro = Parceiro.objects.filter(nome__icontains=form.cleaned_data['nome'])

            return render(request, self.template, {'parceiros': parceiro, 'form': form})
        else:
            form = Busca(request.POST)
            parceiro = Parceiro.objects.all()
        return render(request, self.template, {'parceiros': parceiro, "form": form})


class VisualizarParceiro(LoginRequiredMixin, View):
    template = "parceiro/visualizar.html"

    def get(self, request, parceiro_id=None):

        if parceiro_id:
            parceiro = Parceiro.objects.get(id=parceiro_id)

        else:
            return render(request, self.template, {})

        return render(request, self.template, {'parceiro': parceiro})

    def post(self, request):

        return render(request, self.template)
