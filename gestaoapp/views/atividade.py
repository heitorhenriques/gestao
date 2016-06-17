from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.atividade import FormAtividade
from gestaoapp.models.atividade import Atividade
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroAtividade(View):

	template = 'atividade/cadastro.html'

	def get(self, request, atividade_id=None):

		if atividade_id:
			nome = Atividade.objects.get(id=atividade_id)
			form = FormAtividade(instance= nome)
			editar=True
		else:
			form = FormAtividade()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, atividade_id=None):
		
		if atividade_id:
			nome = Atividade.objects.get(id=atividade_id)
			form = FormAtividade(instance=nome, data=request.POST)
		else:

			form = FormAtividade(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')

		else:
			return render(request, self.template, {'form': form})
			
class ConsultaAtividade(LoginRequiredMixin, View):

	template = 'atividade/consulta.html'
	def get(self, request):
		form = Busca()
		atividade = Atividade.objects.all()

		return render(request, self.template, {'atividades': atividade ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			atividade = Atividade.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'atividades': atividade, 'form':form})
		else:
			form = Busca(request.POST)				
			atividade = Atividade.objects.all()
		return render(request, self.template, {'atividades': atividade,"form": form})

class VisualizarAtividade(LoginRequiredMixin, View):
	
	template = "atividade/visualizar.html"
	
	def get(self, request, atividade_id=None):
		
		if atividade_id:
			atividade = Atividade.objects.get(id=atividade_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'atividade': atividade})
	
	def post(self, request):
		
		return render(request, self.template)