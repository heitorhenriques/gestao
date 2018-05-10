from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.artefato import FormArtefato
from gestaoapp.models.artefato import Artefato
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroArtefato(LoginRequiredMixin,View):

	template = 'artefato/cadastro.html'

	def get(self, request, artefato_id=None):

		if artefato_id:
			nome = Artefato.objects.get(id=artefato_id)
			form = FormArtefato(instance= nome)
			editar=True
		else:
			form = FormArtefato()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, artefato_id=None):
		
		if artefato_id:
			nome = Artefato.objects.get(id=artefato_id)
			form = FormArtefato(instance=nome, data=request.POST)
		else:
			form = FormArtefato(request.POST)
			
		if form.is_valid():
			form.save(request)
			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})

class ConsultaArtefato(LoginRequiredMixin, View):

	template = 'artefato/consulta.html'
	def get(self, request):
		form = Busca()
		artefato = Artefato.objects.all()

		return render(request, self.template, {'artefatos': artefato ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			artefato = Artefato.objects.filter(nome__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'artefatos': artefato, 'form':form})
		else:
			form = Busca(request.POST)				
			artefato = Artefato.objects.all()
		return render(request, self.template, {'artefatos': artefato,"form": form})

class VisualizarArtefato(LoginRequiredMixin, View):
	
	template = "artefato/visualizar.html"
	
	def get(self, request, artefato_id=None):
		
		if artefato_id:
			artefato = Artefato.objects.get(id=artefato_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'artefato': artefato})
	
	def post(self, request):
		
		return render(request, self.template)