# encoding: utf-8
from django.shortcuts import render
from django.views.generic.base import View

from gestaoapp.controls import TabelaHorarios
from gestaoapp.forms.busca import Busca
from gestaoapp.forms.usuario import FormUsuario, FormUsuarioEdit
from gestaoapp.models import Horario
from gestaoapp.models import Vinculo
from gestaoapp.models.usuario import Usuario
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroUsuario(View):
    template = 'usuario/cadastro.html'

    def get(self, request, usuario_id=None):

        if usuario_id:
            nome = Usuario.objects.get(id=usuario_id)
            form = FormUsuarioEdit(instance=nome)
            editar = True
        else:
            form = FormUsuario()
            editar = False

        return render(request, self.template, {'form': form, 'editar': editar})

    def post(self, request, usuario_id=None):

        if usuario_id:
            nome = Usuario.objects.get(id=usuario_id)
            form = FormUsuarioEdit(instance=nome, data=request.POST)
        else:
            print(request.FILES)
            form = FormUsuario(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            user = form.save()
            if 'foto' in request.FILES:
                user.foto = request.FILES['foto']
            user.save()

            msg = "Operação realizada com sucesso!"
            form = FormUsuario()

            return render(request, self.template, {'form': form, 'msg': msg})
            # return redirect('/sucesso')

        else:
            return render(request, self.template, {'form': form})

class AdministrarUsuario(LoginRequiredMixin, View):
    template = 'usuario/desbloquear.html'

    def get(self, request):
        form = Busca()
        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, "form": form})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.filter(titulo__icontains=form.cleaned_data['nome'])

            return render(request, self.template, {'usuarios': usuario, 'form': form})
        else:
            form = Busca(request.POST)
            usuario = Usuario.objects.all()
        return render(request, self.template, {'usuarios': usuario, "form": form})


class ConsultaUsuario(LoginRequiredMixin, View):
    template = 'usuario/consulta.html'

    def get(self, request):
        form = Busca()
        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, "form": form})

    def post(self, request):
        form = Busca(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.filter(first_name__icontains=form.cleaned_data['nome'])

            return render(request, self.template, {'usuarios': usuario, 'form': form})
        else:
            form = Busca(request.POST)
            usuario = Usuario.objects.all()
        return render(request, self.template, {'usuarios': usuario, "form": form})


class VisualizarUsuario(LoginRequiredMixin, View):
    template = "usuario/visualizar.html"

    def get(self, request, usuario_id=None):

        if usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            horarios = TabelaHorarios().get(usuario)
            vinculos = Vinculo.objects.filter(usuario=usuario)
            return render(request, self.template, {'usuario': usuario, 'horarios': horarios, 'vinculos': vinculos})
        else:
            return render(request, self.template, {})

    def post(self, request):

        return render(request, self.template)


class LiberarUsuario(LoginRequiredMixin, View):
    template = 'usuario/desbloquear.html'

    def get(self, request, usuario_verificacao=None):
        if usuario_verificacao:
            nome = Usuario.objects.get(verificacao=usuario_verificacao)
            nome.is_active = True
            nome.save()
            msg = "Usuario Desbloqueado!"
        else:
            msg = "ERRO!"
        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, 'msg': msg})


class BloquearUsuario(LoginRequiredMixin, View):
    template = 'usuario/desbloquear.html'

    def get(self, request, usuario_verificacao=None):
        if usuario_verificacao:
            nome = Usuario.objects.get(verificacao=usuario_verificacao)
            nome.is_active = False
            nome.save()
            msg = "Usuario Bloqueado!"
        else:
            msg = "ERRO!"

        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, 'msg': msg})


class AdmOn(LoginRequiredMixin, View):
    template = 'usuario/desbloquear.html'

    def get(self, request, usuario_verificacao=None):
        if usuario_verificacao:
            nome = Usuario.objects.get(verificacao=usuario_verificacao)
            nome.is_superuser = True
            nome.save()
            msg = "Permissão de Administrador Atribuida"
        else:
            msg = "ERRO!"

        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, 'msg': msg})


class AdmOff(LoginRequiredMixin, View):
    template = 'usuario/desbloquear.html'

    def get(self, request, usuario_verificacao=None):
        if usuario_verificacao:
            nome = Usuario.objects.get(verificacao=usuario_verificacao)
            nome.is_superuser = False
            nome.save()
            msg = "Permissão de Administrador Removida"
        else:
            msg = "ERRO!"

        usuario = Usuario.objects.all()

        return render(request, self.template, {'usuarios': usuario, 'msg': msg})
