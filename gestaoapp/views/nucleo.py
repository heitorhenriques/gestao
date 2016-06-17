from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.nucleo import FormNucleo
from gestaoapp.models.nucleo import Nucleo
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroNucleo(LoginRequiredMixin,View):

	template = 'nucleo/cadastro.html'

	def get(self, request, nucleo_id=None):

		if nucleo_id:
			nome = Nucleo.objects.get(id=nucleo_id)
			form = FormNucleo(instance= nome)
			editar=True
		else:
			form = FormNucleo()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, nucleo_id=None):
		
		if nucleo_id:
			nome = Nucleo.objects.get(id=nucleo_id)
			form = FormNucleo(instance=nome, data=request.POST)
		else:
			form = FormNucleo(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})

class ConsultaNucleo(LoginRequiredMixin, View):

	template = 'nucleo/consulta.html'
	def get(self, request):
		form = Busca()
		nucleo = Nucleo.objects.all()

		return render(request, self.template, {'nucleos': nucleo ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			nucleo = Nucleo.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'nucleos': nucleo, 'form':form})
		else:
			form = Busca(request.POST)				
			nucleo = Nucleo.objects.all()
		return render(request, self.template, {'nucleos': nucleo,"form": form})

class VisualizarNucleo(LoginRequiredMixin, View):
	
	template = "nucleo/visualizar.html"
	
	def get(self, request, nucleo_id=None):
		
		if nucleo_id:
			nucleo = Nucleo.objects.get(id=nucleo_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'nucleo': nucleo})
	
	def post(self, request):
		
		return render(request, self.template)