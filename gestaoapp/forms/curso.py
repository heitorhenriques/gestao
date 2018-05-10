from django import forms

from gestaoapp.models import Curso


class FormCursoCad(forms.ModelForm):
    class Meta:
        model = Curso
        # fields = "__all__"
        exclude = ('responsavel_cadastro',)

class FormCursoEdit(forms.ModelForm):
    class Meta:
        model = Curso
        # fields = "__all__"
        exclude = ('responsavel_cadastro',)
