from django.shortcuts import render, redirect
from django.views.generic.base import View

from gestaoapp.forms.busca import Busca
from gestaoapp.forms.curso import FormCurso
from gestaoapp.models.curso import Curso
from gestaoapp.views.loginrequired import LoginRequiredMixin


class CadastroCurso(LoginRequiredMixin, View):

	template = 'curso/cadastro.html'

	def get(self, request, curso_id=None):

		if curso_id:
			curso = Curso.objects.get(id=curso_id)
			form = FormCurso(instance= curso)
			editar=True
		else:
			form = FormCurso()
			editar=False
		
		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, curso_id=None):
		
		if curso_id:
			curso = Curso.objects.get(id=curso_id)
			form = FormCurso(instance=curso, data=request.POST)
		else:

			form = FormCurso(request.POST)

		if form.is_valid():
			form.save(request)

			return redirect('/cadastro_sucesso')
		else:
			return render(request, self.template, {'form': form})

class ConsultaCurso(LoginRequiredMixin, View):

	template = 'curso/consulta.html'
	def get(self, request):
		form = Busca()
		curso = Curso.objects.all()

		return render(request, self.template, {'cursos': curso ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			curso = Curso.objects.filter(nome__icontains=form.cleaned_data['curso'])

			return render(request, self.template, {'cursos': curso, 'form':form})
		else:
			form = Busca(request.POST)				
			curso = Curso.objects.all()
		return render(request, self.template, {'cursos': curso,"form": form})

class VisualizarCurso(LoginRequiredMixin, View):
	
	template = "curso/visualizar.html"
	
	def get(self, request, curso_id=None):
		
		if curso_id:
			curso = Curso.objects.get(id=curso_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'curso': curso})
	
	def post(self, request):
		
		return render(request, self.template)