from django import forms
from django.db.models import Q

from gestaoapp.models import Horario


class FormHorario(forms.ModelForm):
    hora_inicio = forms.TimeField(label='hora_inicio')
    hora_fim = forms.TimeField(label='hora_fim')
    usuario = forms.CharField(required=False)

    def verifica_horario(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fim = self.cleaned_data.get('hora_fim')

        if hora_inicio >= hora_fim:
            raise forms.ValidationError('Horario Invalido')

        return self

    def horario_sem_conflito(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_fim = self.cleaned_data.get('hora_fim')
        data = self.cleaned_data.get('data')

        busca = Horario.objects.filter(Q(data=data) & Q(usuario=self.usuario), Q(hora_inicio__range=[hora_inicio, hora_fim]) | Q(hora_fim__range=[hora_inicio, hora_fim])).count()
        if busca > 0:
            raise forms.ValidationError('Horario conflitante')

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