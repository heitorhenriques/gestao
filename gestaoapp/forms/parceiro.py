from django import forms

from gestaoapp.models import Parceiro


class FormParceiro(forms.ModelForm):
    class Meta:
        model = Parceiro
        # fields = "__all__"
        exclude = ('responsavel_cadastro',)

class FormParceiroEdit(forms.ModelForm):
    class Meta:
        model = Parceiro
        # fields = "__all__"
        exclude = ('responsavel_cadastro',)