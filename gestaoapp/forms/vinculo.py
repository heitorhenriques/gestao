from django import forms
from gestaoapp.models import Vinculo

class FormVinculo(forms.ModelForm):

    dt_inicio = forms.DateField(label='dt_inicio')
    dt_termino = forms.DateField(label='dt_termino')

    class Meta:
        model = Vinculo
        fields = '__all__'

