from django import forms
from gestaoapp.models import Nucleo

class FormNucleo(forms.ModelForm):

	class Meta:
		model = Nucleo
		fields = "__all__" 