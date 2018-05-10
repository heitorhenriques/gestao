from django import forms
from gestaoapp.models import Projeto

class FormProjetoMembro(forms.ModelForm):

	class Meta:
		model = Projeto
		#fields = "membro" 
		exclude = ('tipo','nome','codigo', 'coordenador','duracao','data_inicio','data_fim','nucleo','edital','descricao', 'data_cadastro','parceiro') 
	