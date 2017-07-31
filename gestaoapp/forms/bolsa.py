from django import forms

from gestaoapp.models import Bolsa


class FormBolsa(forms.ModelForm):
    class Meta:
        model = Bolsa
        fields = "__all__"


class FormBolsaEdit(forms.ModelForm):
    class Meta:
        model = Bolsa
        fields = "__all__"
