from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import password_reset
from gestaoapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^troca_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'troca.html'}, name='troca_senha'),
    
    url(r'^home/', home),

    url(r'^usuario/', CadastroUsuario.as_view(), name='usuario'),
    url(r'^editar_usuario/(?P<usuario_id>\d+)/$', CadastroUsuario.as_view()),
    url(r'^desbloquear_usuario/', AdministrarUsuario.as_view()),
    url(r'^consulta_usuario/', ConsultaUsuario.as_view()),
    url(r'^visualizar_usuario/(?P<usuario_id>\d+)/$', VisualizarUsuario.as_view()),
    url(r'^liberar_usuario/(?P<usuario_verificacao>\w+)/$', LiberarUsuario.as_view()),
    url(r'^bloquear_usuario/(?P<usuario_verificacao>\w+)/$', BloquearUsuario.as_view()),
    url(r'^adm_on/(?P<usuario_verificacao>\w+)/$', AdmOn.as_view()),
    url(r'^adm_off/(?P<usuario_verificacao>\w+)/$', AdmOff.as_view()),

    url(r'^horario/', CadastroHorario.as_view()),
    url(r'^excluir_horario/(?P<horario_id>\d+)/$', ExcluirHorario.as_view()),    
    url(r'^editar_horario/(?P<horario_id>\d+)/$', CadastroHorario.as_view()),
    url(r'^hora_invalida/', hora_invalida),

    url(r'^curso/', CadastroCurso.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),
    url(r'^editar_projeto/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),
    url(r'^consulta_projeto/', ConsultaProjeto.as_view()),
    url(r'^visualizar_projeto/(?P<projeto_id>\d+)/$', VisualizarProjeto.as_view()),
    #url(r'^horaprojeto/', CadastroHoraProjeto.as_view()),

    url(r'^nucleo/', CadastroNucleo.as_view()),
    url(r'^editar_nucleo/(?P<nucleo_id>\d+)/$', CadastroNucleo.as_view()),
    url(r'^consulta_nucleo/', ConsultaNucleo.as_view()),
    url(r'^visualizar_nucleo/(?P<nucleo_id>\d+)/$', VisualizarNucleo.as_view()),

    url(r'^sucesso/', sucesso),
    url(r'^cadastro_sucesso/', cadastro_sucesso),

    url(r'^recurso/', CadastroRecurso.as_view()),
    url(r'^editar_recurso/(?P<recurso_id>\d+)/$', CadastroRecurso.as_view()),
    url(r'^tipo_recurso/', CadastroTipoRecurso.as_view()),
    url(r'^editar_tipo_recurso/', CadastroTipoRecurso.as_view()),
    url(r'^consulta_recurso/', ConsultaRecurso.as_view()),
    url(r'^visualizar_recurso/(?P<recurso_id>\d+)/$', VisualizarRecurso.as_view()),

    url(r'^artefato/', CadastroArtefato.as_view()),
    url(r'^editar_artefato/(?P<artefato_id>\d+)/$', CadastroArtefato.as_view()),
    url(r'^consulta_artefato/', ConsultaArtefato.as_view()),
    url(r'^visualizar_artefato/(?P<artefato_id>\d+)/$', VisualizarArtefato.as_view()),
    
    url(r'^atividade/', CadastroAtividade.as_view()),
    url(r'^editar_atividade/(?P<atividade_id>\d+)/$', CadastroAtividade.as_view()),
    url(r'^consulta_atividade/', ConsultaAtividade.as_view()),
    url(r'^visualizar_atividade/(?P<atividade_id>\d+)/$', VisualizarAtividade.as_view()),

    url(r'^edital/', CadastroEdital.as_view()),
    url(r'^editar_edital/(?P<edital_id>\d+)/$', CadastroEdital.as_view()),
    url(r'^consulta_edital/', ConsultaEdital.as_view()),
    url(r'^visualizar_edital/(?P<edital_id>\d+)/$', VisualizarEdital.as_view()),

]
