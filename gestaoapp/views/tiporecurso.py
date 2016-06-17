from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.tiporecurso import FormTipoRecurso
from gestaoapp.models.tiporecurso import TipoRecurso
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroTipoRecurso(LoginRequiredMixin,View):

	template = 'recurso/tipo/cadastro.html'

	def get(self, request, tiporecurso_id=None):

		if tiporecurso_id:
			nome = TipoRecurso.objects.get(id=tiporecurso_id)
			form = FormTipoRecurso(instance= nome)
			editar=True
		else:
			form = FormTipoRecurso()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, tiporecurso_id=None):
		
		if tiporecurso_id:
			nome = TipoRecurso.objects.get(id=tiporecurso_id)
			form = FormTipoRecurso(instance=nome, data=request.POST)
		else:
			form = FormTipoRecurso(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})