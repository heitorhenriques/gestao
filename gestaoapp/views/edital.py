from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.edital import FormEdital
from gestaoapp.models.edital import Edital
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroEdital(LoginRequiredMixin, View):

	template = 'edital/cadastro.html'

	def get(self, request, edital_id=None):

		if edital_id:
			edital = Edital.objects.get(id=edital_id)
			form = FormEdital(instance= edital)
			editar=True
		else:
			form = FormEdital()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, edital_id=None):
		
		if edital_id:
			edital = Edital.objects.get(id=edital_id)
			form = FormEdital(instance=edital, data=request.POST)
		else:

			form = FormEdital(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/cadastro_sucesso')

		else:
			return render(request, self.template, {'form': form})

class ConsultaEdital(LoginRequiredMixin, View):

	template = 'edital/consulta.html'
	def get(self, request):
		form = Busca()
		edital = Edital.objects.all()

		return render(request, self.template, {'editals': edital ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			edital = Edital.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'editals': edital, 'form':form})
		else:
			form = Busca(request.POST)				
			edital = Edital.objects.all()
		return render(request, self.template, {'editals': edital,"form": form})

class VisualizarEdital(LoginRequiredMixin, View):
	
	template = "edital/visualizar.html"
	
	def get(self, request, edital_id=None):
		
		if edital_id:
			edital = Edital.objects.get(id=edital_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'edital': edital})
	
	def post(self, request):
		
		return render(request, self.template)