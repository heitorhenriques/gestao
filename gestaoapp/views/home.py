# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
import logging

from gestaoapp.models.projeto import Projeto


class Home(View):
    template = 'home/index.html'

    def get(self, request):
        if request.user.is_authenticated():

            projeto_membro = Projeto.objects.filter(membro=request.user.id)
            projeto_coordenador = Projeto.objects.filter(coordenador=request.user.id)

            return render(request, self.template, {'projeto_membro': projeto_membro, 'projeto_coordenador': projeto_coordenador})
            # return render(request, self.template, {})
        else:
            return HttpResponseRedirect('/login/')
