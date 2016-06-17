from django import forms
from gestaoapp.models import Recurso

class FormRecurso(forms.ModelForm):

	class Meta:
		model = Recurso
		fields = "__all__" 