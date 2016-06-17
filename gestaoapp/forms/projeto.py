from django import forms
from gestaoapp.models import Projeto

class FormProjeto(forms.ModelForm):
	data_inicio = forms.DateField(label='date_inicio')
	data_fim = forms.DateField(label='date_fim')

	class Meta:
		model = Projeto
		fields = "__all__"