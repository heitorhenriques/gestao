from django import forms

from gestaoapp.models import Edital


class FormEdital(forms.ModelForm):
    dt_inicio = forms.DateField(label='dt_inicio')
    dt_termino = forms.DateField(label='dt_termino')

    class Meta:
        model = Edital
        fields = "__all__"


class FormEditalEdit(forms.ModelForm):
    class Meta:
        model = Edital
        fields = "__all__"
