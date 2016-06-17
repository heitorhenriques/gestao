from django import forms
from gestaoapp.models import Artefato

class FormArtefato(forms.ModelForm):

	class Meta:
		model = Artefato
		fields = "__all__" 