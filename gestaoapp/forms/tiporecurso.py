from django import forms
from gestaoapp.models import TipoRecurso

class FormTipoRecurso(forms.ModelForm):

	class Meta:
		model = TipoRecurso
		fields = "__all__" 