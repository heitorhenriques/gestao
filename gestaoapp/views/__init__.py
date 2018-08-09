from django.shortcuts import render

from gestaoapp.views.artefato import CadastroArtefato, ConsultaArtefato, VisualizarArtefato
from gestaoapp.views.atividade import CadastroAtividade, ConsultaAtividade, VisualizarAtividade
from gestaoapp.views.bolsa import CadastroBolsa, ConsultaBolsa, VisualizarBolsa
from gestaoapp.views.curso import CadastroCurso, ConsultaCurso, VisualizarCurso
from gestaoapp.views.edital import CadastroEdital, ConsultaEdital, VisualizarEdital
from gestaoapp.views.home import Home
from gestaoapp.views.horario import CadastroHorario, ExcluirHorario, ApresentarHorarios
from gestaoapp.views.nucleo import CadastroNucleo, ConsultaNucleo, VisualizarNucleo
from gestaoapp.views.parceiro import CadastroParceiro, ConsultaParceiro, VisualizarParceiro
from gestaoapp.views.projeto import CadastroProjeto, ConsultaProjeto, VisualizarProjeto, AddMembro
from gestaoapp.views.recurso import CadastroRecurso, ConsultaRecurso, VisualizarRecurso
from gestaoapp.views.tiporecurso import CadastroTipoRecurso
from gestaoapp.views.usuario import CadastroUsuario, ConsultaUsuario, VisualizarUsuario, AdministrarUsuario, \
    LiberarUsuario, BloquearUsuario, AdmOn, AdmOff
from gestaoapp.views.vinculo import CadastroVinculo, CadastroVinculoBolsa
from gestaoapp.views.logcadastro import LogCadastro
from gestaoapp.views.pagamentos import CadastroPagamento, ConsultaPagamento
from gestaoapp.views.verificacao_pagamento import verifica


def sucesso(request):
    return render(request, 'usuario/aguarde_liberacao.html')

def cadastro_liberado(request):
    return render(request, 'usuario/cadastro_liberado.html')

def cadastros(request):
    return render(request, 'mobile/cadastro.html')

# def home(request):
# 	return render(request, 'home/index.html')

def cadastro_sucesso(request):
    return render(request, 'sucesso.html')


def hora_invalida(request):
    return render(request, 'horario/invalida.html')
