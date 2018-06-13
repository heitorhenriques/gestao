from django import forms
from gestaoapp.models.pagamentos import Pagamentos


class FormPagamento(forms.ModelForm):
    class Meta:
        model = Pagamentos
        fields = ['dt_pagamento', 'valor', 'vinculo']