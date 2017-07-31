# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse

from gestaoapp.forms.horario import FormHorario, FormHorarioEdit
from gestaoapp.models.horario import Horario
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroHorario(LoginRequiredMixin, View):
    template = 'horario/cadastro.html'

    def get(self, request, horario_id=None):
        horarios = self.getHorarios(request)

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

        horarios = self.getHorarios(request)
        return render(request, self.template, {'form': form, 'msg': msg, 'edit': edit, 'horarios': horarios})


    def getHorarios(self, request):
        horarios = Horario.objects.filter(usuario=Usuario.objects.get(pk=request.user.id)).order_by('hora_inicio', 'hora_fim')
        return self.organizarHorarios(horarios)

    def organizarHorarios(self, horarios):
        horarios_organizados_por_dia = {}
        for horario in horarios:
            if horario.data in horarios_organizados_por_dia:
                horarios_organizados_por_dia[horario.data].append(horario)
            else:
                horarios_organizados_por_dia[horario.data] = [horario]
        return horarios_organizados_por_dia

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