from django import forms
from gestaoapp.models import Curso

class FormCurso(forms.ModelForm):

	class Meta:
		model = Curso
		fields = "__all__" 