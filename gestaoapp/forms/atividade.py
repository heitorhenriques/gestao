from django import forms
from gestaoapp.models import Atividade

class FormAtividade(forms.ModelForm):

	class Meta:
		model = Atividade
		fields = "__all__" 