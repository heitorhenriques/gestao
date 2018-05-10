from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User

from gestaoapp.models.projeto import Projeto
from gestaoapp.models.usuario import Usuario
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.models.edital import Edital
from gestaoapp.models.curso import Curso
from gestaoapp.models.parceiro import Parceiro
from gestaoapp.models.bolsa import Bolsa

from gestaoapp.views.loginrequired import LoginRequiredMixin


class Relatorio2(LoginRequiredMixin, View):
    template = "relatorio/visualizar.html"

    def get(self, request, projeto_id=None):

        if projeto_id:
            projeto = Projeto.objects.get(id=projeto_id)
            membro = Usuario.objects.get(id=request.user.id)
        else:
            return render(request, self.template, {})

        return render(request, self.template, {'projeto': projeto, 'membro': membro})

    def post(self, request):

        return render(request, self.template)

class LogCadastro(LoginRequiredMixin, View):
        template = 'relatorio/visualizar.html'

        def get(self, request):

            projeto = Projeto.objects.all()
            usuario = User.objects.all()
            nucleo = Nucleo.objects.all()
            edital = Edital.objects.all()
            curso = Curso.objects.all()
            parceiro = Parceiro.objects.all()
            bolsa = Bolsa.objects.all()

            return render(request, self.template, {'projetos': projeto, 'usuario': usuario, 'nucleos': nucleo, 'editals': edital, 'cursos': curso, 'bolsas':bolsa, 'parceiros':parceiro })