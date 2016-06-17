from django import forms


class Busca(forms.Form):
	nome = forms.CharField(label='Buscar', widget=forms.TextInput)