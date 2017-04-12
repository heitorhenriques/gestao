from django import forms

from gestaoapp.models import Parceiro


class FormParceiro(forms.ModelForm):
    class Meta:
        model = Parceiro
        fields = "__all__"


class FormParceiroEdit(forms.ModelForm):
    class Meta:
        model = Parceiro
        fields = "__all__"
