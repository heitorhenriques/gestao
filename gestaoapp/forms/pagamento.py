from django import forms
from gestaoapp.models.pagamentos import Pagamentos

class FormPagamento(forms.ModelForm):

    dt_pagamento = forms.DateField(label='dt_pagamento')

    class Meta:
        model = Pagamentos
        fields = '__all__'
        # fields = ('vinculo',)