# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User

from gestaoapp.forms.busca import Busca
from gestaoapp.forms.curso import FormCursoCad, FormCursoEdit
from gestaoapp.models.curso import Curso
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroCurso(LoginRequiredMixin, View):
    template = 'curso/cadastro.html'

    def get(self, request, curso_id=None):

        if curso_id:
            curso = Curso.objects.get(id=curso_id)
            form = FormCursoEdit(instance=curso)
            editar = True
        else:
            form = FormCursoCad()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar})

    def post(self, request, curso_id=None):

        if curso_id:
            curso = Curso.objects.get(id=curso_id)
            form = FormCursoEdit(instance=curso, data=request.POST)
        else:

            form = FormCursoCad(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.responsavel_cadastro = User.objects.get(pk=request.user.id)
            post.save()
            form.save(request)
            msg = 'Operação realizada com sucesso!'
            form = FormCursoCad()
            return render(request, self.template, {'form': form, 'msg': msg})
        else:
            return render(request, self.template, {'form': form})


class ConsultaCurso(LoginRequiredMixin, View):
    template = 'curso/consulta.html'

    def get(self, request):
        form = Busca()
        curso = Curso.objects.all()

        return render(request, self.template, {'cursos': curso, "form": form})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            curso = Curso.objects.filter(nome__icontains=form.cleaned_data['curso'])

            return render(request, self.template, {'cursos': curso, 'form': form})
        else:
            form = Busca(request.POST)
            curso = Curso.objects.all()
        return render(request, self.template, {'cursos': curso, "form": form})


class VisualizarCurso(LoginRequiredMixin, View):
    template = "curso/visualizar.html"

    def get(self, request, curso_id=None):

        if curso_id:
            curso = Curso.objects.get(id=curso_id)

        else:
            return render(request, self.template, {})

        return render(request, self.template, {'curso': curso})

    def post(self, request):

        return render(request, self.template)
