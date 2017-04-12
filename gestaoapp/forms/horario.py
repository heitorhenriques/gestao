from django import forms

from gestaoapp.models import Horario


class FormHorario(forms.ModelForm):
    hora_inicio = forms.TimeField(label='hora_inicio')
    hora_fim = forms.TimeField(label='hora_fim')

    def verifica_horario(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fim = self.cleaned_data.get('hora_fim')

        if hora_inicio >= hora_fim:
            raise forms.ValidationError('Horario Invalido')

        return self

    class Meta:
        model = Horario
        fields = "__all__"


class FormHorarioEdit(forms.ModelForm):
    def verifica_horario(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fim = self.cleaned_data.get('hora_fim')

        if hora_inicio >= hora_fim:
            raise forms.ValidationError('Horario Invalido')

        return self

    class Meta:
        model = Horario
        fields = "__all__"
