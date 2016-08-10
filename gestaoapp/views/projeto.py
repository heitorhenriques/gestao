from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.projeto import FormProjeto
from gestaoapp.models.projeto import Projeto
from gestaoapp.models.usuario import Usuario
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroProjeto(LoginRequiredMixin,View):

	template = 'projeto/cadastro.html'

	def get(self, request, projeto_id=None):

		if projeto_id:
			nome = Projeto.objects.get(id=projeto_id)
			form = FormProjeto(instance= nome)
			editar=True
		else:
			form = FormProjeto()
			usuarios = Usuario.objects.filter(is_superuser=True) and Usuario.objects.filter(is_active =True)
			editar = False
		
		return render(request, self.template, {'form': form,'editar':editar, 'usuarios':usuarios})

	def post(self, request, projeto_id=None):
		
		if projeto_id:
			nome = Projeto.objects.get(id=projeto_id)
			form = FormProjeto(instance=nome, data=request.POST)
		else:
			form = FormProjeto(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})

class ConsultaProjeto(LoginRequiredMixin, View):

	template = 'projeto/consulta.html'
	def get(self, request):
		form = Busca()
		projeto = Projeto.objects.all()

		return render(request, self.template, {'projetos': projeto ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			projeto = Projeto.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'projetos': projeto, 'form':form})
		else:
			form = Busca(request.POST)				
			projeto = Projeto.objects.all()
		return render(request, self.template, {'projetos': projeto,"form": form})

class VisualizarProjeto(LoginRequiredMixin, View):
	
	template = "projeto/visualizar.html"
	
	def get(self, request, projeto_id=None):
		
		if projeto_id:
			projeto = Projeto.objects.get(id=projeto_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'projeto': projeto})
	
	def post(self, request):
		
		return render(request, self.template)