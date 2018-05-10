from django import forms
from django.db.models import Count
from gestaoapp.models import Bolsa, Edital


class FormBolsa(forms.ModelForm):
    dt_inicio = forms.DateField(label='dt_inicio')
    dt_termino = forms.DateField(label='dt_termino')

    class Meta:
        model = Bolsa
        exclude = ('vinculos', 'responsavel_cadastro', 'responsavel_gerencia',)

    # def __init__(self, *args, **kwargs):
        # super(FormBolsa, self).__init__(*args, **kwargs)

        # bolsas_por_edital = Bolsa.objects.values('edital', 'edital__qtd_bolsa').annotate(Count('edital__id'))
        # print(bolsas_por_edital)
        # editais = [b['edital'] for b in bolsas_por_edital if b['edital__id__count'] < b['edital__qtd_bolsa']]

        # self.fields['edital'].queryset = Edital.objects.filter(id__in=editais)

class FormBolsaPorEdital(forms.ModelForm):
    dt_inicio = forms.DateField(label='dt_inicio')
    dt_termino = forms.DateField(label='dt_termino')
    edital = forms.ChoiceField(required=False)

    class Meta:
        model = Bolsa
        exclude = ('vinculos', 'responsavel_cadastro', 'responsavel_gerencia')

class FormBolsaEdit(forms.ModelForm):
    class Meta:
        model = Bolsa
        exclude = ('vinculos','responsavel_cadastro', 'responsavel_gerencia', )