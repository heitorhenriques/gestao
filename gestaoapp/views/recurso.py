from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.recurso import FormRecurso
from gestaoapp.models.recurso import Recurso
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroRecurso(LoginRequiredMixin,View):

	template = 'recurso/cadastro.html'

	def get(self, request, recurso_id=None):

		if recurso_id:
			nome = Recurso.objects.get(id=recurso_id)
			form = FormRecurso(instance= nome)
			editar=True
		else:
			form = FormRecurso()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, recurso_id=None):
		
		if recurso_id:
			nome = Recurso.objects.get(id=recurso_id)
			form = FormRecurso(instance=nome, data=request.POST)
		else:
			form = FormRecurso(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})

class ConsultaRecurso(LoginRequiredMixin, View):

	template = 'recurso/consulta.html'
	def get(self, request):
		form = Busca()
		recurso = Recurso.objects.all()

		return render(request, self.template, {'recursos': recurso ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			recurso = Recurso.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'recursos': recurso, 'form':form})
		else:
			form = Busca(request.POST)				
			recurso = Recurso.objects.all()
		return render(request, self.template, {'recursos': recurso,"form": form})

class VisualizarRecurso(LoginRequiredMixin, View):
	
	template = "recurso/visualizar.html"
	
	def get(self, request, recurso_id=None):
		
		if recurso_id:
			recurso = Recurso.objects.get(id=recurso_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'recurso': recurso})
	
	def post(self, request):
		
		return render(request, self.template)