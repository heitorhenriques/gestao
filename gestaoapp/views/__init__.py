from django.shortcuts import render
from django.template import RequestContext
from gestaoapp.views.usuario import CadastroUsuario, ConsultaUsuario, VisualizarUsuario, AdministrarUsuario, LiberarUsuario
from gestaoapp.views.horario import CadastroHorario, ExcluirHorario
from gestaoapp.views.projeto import CadastroProjeto, ConsultaProjeto, VisualizarProjeto
from gestaoapp.views.nucleo	import CadastroNucleo, ConsultaNucleo, VisualizarNucleo
from gestaoapp.views.recurso import CadastroRecurso, ConsultaRecurso, VisualizarRecurso
from gestaoapp.views.tiporecurso import CadastroTipoRecurso
from gestaoapp.views.artefato import CadastroArtefato, ConsultaArtefato, VisualizarArtefato
from gestaoapp.views.atividade import CadastroAtividade, ConsultaAtividade, VisualizarAtividade
from gestaoapp.views.edital import CadastroEdital, ConsultaEdital, VisualizarEdital
from gestaoapp.views.curso import CadastroCurso, ConsultaCurso, VisualizarCurso


def sucesso(request):
	return render(request, 'usuario/aguarde_liberacao.html')

def cadastro_liberado(request):
	return render(request, 'usuario/cadastro_liberado.html')

def home(request):
	return render(request, 'home/index.html')

def cadastro_sucesso(request):
	return render(request, 'sucesso.html')

def hora_invalida(request):
	return render(request, 'horario/invalida.html')
