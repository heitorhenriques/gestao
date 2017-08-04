from django import forms
from gestaoapp.models import Vinculo

class FormVinculo(forms.ModelForm):

    dt_inicio = forms.DateField(label='dt_inicio')
    dt_termino = forms.DateField(label='dt_termino')

    class Meta:
        model = Vinculo
        fields = '__all__'

class FormVinculoBolsa(forms.ModelForm):

    dt_inicio = forms.DateField(label='dt_inicio')
    status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked': True}))

    class Meta:
        model = Vinculo
        fields = ['dt_inicio', 'usuario', 'status']