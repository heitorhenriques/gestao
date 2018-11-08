# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
from gestaoapp.models import Vinculo,Projeto
from gestaoapp.controls import TabelaHorarios
from gestaoapp.forms.horario import FormHorario, FormHorarioEdit
from gestaoapp.models.horario import Horario
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroHorario(LoginRequiredMixin, View):
    template = 'horario/cadastro.html'

    def get(self, request, horario_id=None):
        horarios = TabelaHorarios().get(request.user.id)

        if horario_id:
            horario_atual = Horario.objects.get(id=horario_id)
            form = FormHorarioEdit(instance=horario_atual)
            editar = True
        else:
            form = FormHorario()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar, 'horarios': horarios})

    def post(self, request, horario_id=None):

        edit = False
        msg = None
        usuario = Usuario.objects.get(pk=request.user.id)

        if horario_id:
            edit = True
            horario_atual = Horario.objects.get(id=horario_id)
            form = FormHorario(data=request.POST, instance=horario_atual)
        else:
            form = FormHorario(data=request.POST)

        form.usuario = usuario
        if form.is_valid() and form.verifica_horario() and form.horario_sem_conflito():
            if edit:
                msg = "Horário editado com sucesso!"
            else:
                msg = "Horário registrado com sucesso!"
            horario = form.save(commit=False)
            horario.usuario = usuario
            horario.save()
        else:
            print(form.errors)

        horarios = TabelaHorarios().get(usuario)
        return render(request, self.template, {'form': form, 'msg': msg, 'edit': edit, 'horarios': horarios})

class ExcluirHorario(LoginRequiredMixin, View):
    def get(self, request, horario_id):
        nome = Horario.objects.get(id=horario_id)
        if nome.id is not None:
            nome.delete()
            return redirect('/horario')


exclude = (
    'last_login', "groups", "user_permissions", "helptext", "is_staff", "date_joined", 'is_active', 'dia', 'mail',
    'verificacao')


class ApresentarHorarios(LoginRequiredMixin, View):

    def get(self, request):
        usuario = Usuario.objects.get(pk=request.user.id)

        horarios = list(Horario.objects.filter(usuario=usuario).values('id', 'hora_inicio', 'hora_fim', 'data', 'turno'))
        return JsonResponse({'data': horarios})

class GerarHorario(LoginRequiredMixin, View):

    def get(self, request):
        usuario = Usuario.objects.get(pk=request.user.id)
        horarios = Horario.objects.filter(usuario=usuario)
        vinculo = Vinculo.objects.get(usuario=usuario)
        projeto = Projeto.objects.get(membro__responsavel__vinculo=vinculo)
        dt_fim = (vinculo.dt_termino.year * 365) + (vinculo.dt_termino.month * 30) + vinculo.dt_termino.day
        dt_inicio = (vinculo.dt_inicio.year * 365) + (vinculo.dt_inicio.month * 30) + vinculo.dt_inicio.day
        tempo = (dt_fim - dt_inicio) / 7
        dt_atual = datetime.now()
        for horario in horarios:
            minutos_fim = (horario.hora_fim.hour * 60) + horario.hora_fim.minute
            minutos_inicio = (horario.hora_inicio.hour * 60) + horario.hora_inicio.minute
            semana = minutos_fim - minutos_inicio
            qtd = semana * tempo
            render(request,'../../paper-css-master/index.html',{'nome_aluno':usuario.first_name,
                                                                'nomeprojeto':projeto.nome,
                                                                'nome_professor':projeto.coordenador,
                                                                'dt_inicio':vinculo.dt_inicio,
                                                                'dt_termino':vinculo.dt_termino,
                                                                'qtd_horas':qtd,
                                                                'ano':dt_atual.year,
                                                                'mes':dt_atual.month,
                                                                'dia':dt_atual.day})