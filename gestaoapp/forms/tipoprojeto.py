from django import forms
from gestaoapp.models import TipoProjeto

class FormTipoProjeto(forms.ModelForm):

	class Meta:
		model = TipoProjeto
		fields = "__all__" 