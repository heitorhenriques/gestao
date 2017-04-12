from django import forms

from gestaoapp.models import Curso


class FormCursoCad(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"


class FormCursoEdit(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
