from django import forms

from gestaoapp.models import Bolsa


class FormBolsa(forms.ModelForm):
    class Meta:
        model = Bolsa
        exclude = ('vinculos', 'status')


class FormBolsaEdit(forms.ModelForm):
    class Meta:
        model = Bolsa
        exclude = ('vinculos', 'status')
