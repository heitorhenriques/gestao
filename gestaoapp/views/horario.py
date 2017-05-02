# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gestaoapp.forms.horario import FormHorario, FormHorarioEdit
from gestaoapp.models.horario import Horario
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroHorario(LoginRequiredMixin, View):
    template = 'horario/cadastro.html'

    def get(self, request, horario_id=None):

        if horario_id:
            nome = Horario.objects.get(id=horario_id)
            form = FormHorarioEdit(instance=nome)
            editar = True
        else:
            form = FormHorario()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar})

    def post(self, request, horario_id=None):

        if horario_id:
            nome = Horario.objects.get(id=horario_id)
            form = FormHorarioEdit(instance=nome, data=request.POST)
        else:
            form = FormHorario(request.POST)

        if form.is_valid() and form.verifica_horario():
            u = Usuario.objects.get(username=request.user.username)

            form = FormHorario(request.POST)
            ini = []

            for h in u.dia.all():
                if str(h.data) == form.data['data']:
                    ini.append(h.hora_inicio.strftime('%H:%M'))

            if not ini:
                print("Dia nao cadastrado")
                dia = form.save(request)
                user = Usuario.objects.get(id=request.user.id)
                user.dia.add(dia)
                msg = "Operação realizada com sucesso!"
            else:
                print("Dia cadastrado!")
                for h in u.dia.all():
                    if str(h.data) == form.data['data']:
                        if (form.data['hora_inicio'] < h.hora_inicio.strftime('%H:%M') and form.data[
                            'hora_fim'] < h.hora_inicio.strftime('%H:%M')) or (
                                        form.data['hora_inicio'] > h.hora_fim.strftime('%H:%M') and form.data[
                                    'hora_fim'] > h.hora_fim.strftime('%H:%M')):
                            print("Horario Valido")
                            dia = form.save(request)
                            user = Usuario.objects.get(id=request.user.id)
                            user.dia.add(dia)

                            msg = "Operação realizada com sucesso!"
                            form = FormHorario()
                            return render(request, self.template, {'form': form, 'msg': msg})
                        else:
                            msg1 = "Horario ja Cadastrado! "

                            return render(request, self.template, {'form': form, 'msg1': msg1})

            return render(request, self.template, {'form': form, 'msg': msg})
                        # return redirect('/cadastro_sucesso')
        else:
            return render(request, self.template, {'form': form})


class ExcluirHorario(LoginRequiredMixin, View):
    def get(self, request, horario_id):
        nome = Horario.objects.get(id=horario_id)
        if nome.id is not None:
            nome.delete()
            return redirect('/horario')


exclude = (
    'last_login', "groups", "user_permissions", "helptext", "is_staff", "date_joined", 'is_active', 'dia', 'mail',
    'verificacao')
