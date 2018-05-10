#coding:utf-8
from gestaoapp.models import Horario

class TabelaHorarios:

    def get(self, usuario):
        horarios = Horario.objects.filter(usuario=usuario).order_by('hora_inicio', 'hora_fim')
        return self.organizarHorarios(horarios)

    def organizarHorarios(self, horarios):
        horarios_organizados_por_dia = {}
        for horario in horarios:
            if horario.data in horarios_organizados_por_dia:
                horarios_organizados_por_dia[horario.data].append(horario)
            else:
                horarios_organizados_por_dia[horario.data] = [horario]
        return horarios_organizados_por_dia