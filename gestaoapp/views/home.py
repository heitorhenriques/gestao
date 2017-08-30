# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
import logging

from gestaoapp.models.projeto import Projeto


class Home(View):
    template = 'home/index.html'


    def get(self, request):
        #logger = logging.getLogger('__name__')
        #logger.info('Testando Django Monitoring Splunk!')
        projeto_membro = Projeto.objects.filter(membro=request.user.id)
        projeto_coordenador = Projeto.objects.filter(coordenador=request.user.id)

        return render(request, self.template,
                      {'projeto_membro': projeto_membro, 'projeto_coordenador': projeto_coordenador})
