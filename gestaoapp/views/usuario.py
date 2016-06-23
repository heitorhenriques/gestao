from django.shortcuts import render, redirect
from django.views.generic.base import View
from gestaoapp.forms.usuario import FormUsuario
from gestaoapp.models.usuario import Usuario
from gestaoapp.forms.busca import Busca
from gestaoapp.views.loginrequired import LoginRequiredMixin

class CadastroUsuario(View):

	template = 'usuario/cadastro.html'

	def get(self, request , usuario_id = None):

		if usuario_id:
			nome = Usuario.objects.get(id =usuario_id)
			form = FormUsuario(instance= nome)
			editar=True
		else:
			form = FormUsuario()
			editar=False

		return render(request, self.template, {'form': form,'editar':editar})

	def post(self, request, usuario_id=None):
		
		if usuario_id:
			nome = Usuario.objects.get(id=usuario_id)
			form = FormUsuario(instance=nome, data=request.POST)
		else:
			print(request.FILES)
			form = FormUsuario(request.POST, request.FILES)

		if form.is_valid():
			form.save(request)
			return redirect('/sucesso')

		else:
			return render(request, self.template, {'form': form})

class AdministrarUsuario(LoginRequiredMixin, View):

	template = 'usuario/desbloquear.html'
	def get(self, request):
		form = Busca()
		usuario = Usuario.objects.all()

		return render(request, self.template, {'usuarios': usuario ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			usuario = Usuario.objects.filter(titulo__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'usuarios': usuario, 'form':form})
		else:
			form = Busca(request.POST)				
			usuario = Usuario.objects.all()
		return render(request, self.template, {'usuarios': usuario,"form": form})

class ConsultaUsuario(LoginRequiredMixin, View):

	template = 'usuario/consulta.html'
	def get(self, request):
		form = Busca()
		usuario = Usuario.objects.all()

		return render(request, self.template, {'usuarios': usuario ,"form": form})
	
	def post(self, request):
		form = Busca(request.POST)
		if form.is_valid():
			usuario = Usuario.objects.filter(first_name__icontains=form.cleaned_data['nome'])

			return render(request, self.template, {'usuarios': usuario, 'form':form})
		else:
			form = Busca(request.POST)				
			usuario = Usuario.objects.all()
		return render(request, self.template, {'usuarios': usuario,"form": form})

class VisualizarUsuario(LoginRequiredMixin, View):
	
	template = "usuario/visualizar.html"
	
	def get(self, request, usuario_id=None):
		
		if usuario_id:
			usuario = Usuario.objects.get(id=usuario_id)

		else:
			return render(request, self.template, { })

		return render(request, self.template, {'usuario': usuario})
	
	def post(self, request):
		
		return render(request, self.template)
		
class LiberarUsuario(LoginRequiredMixin,View):

	template = 'usuario/conta_desbloqueada.html'

	def get(self, request, usuario_verificacao = None):

		if usuario_verificacao:
			nome = Usuario.objects.get(verificacao =usuario_verificacao)
			nome.is_active = True
			nome.save()
			
		return render(request, self.template)

class AdmOn(LoginRequiredMixin,View):

	template = 'usuario/conta_desbloqueada.html'

	def get(self, request, usuario_verificacao = None):

		if usuario_verificacao:
			nome = Usuario.objects.get(verificacao =usuario_verificacao)
			nome.is_superuser = True
			nome.save()
			
		return render(request, self.template)