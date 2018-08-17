from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from gestaoapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^alterar_senha/$', 'django.contrib.auth.views.password_change', {'template_name': 'troca.html'},
        name='password_change_done'),

    url(r'^$','django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^home/', Home.as_view()),

    url(r'^usuario/', CadastroUsuario.as_view(), name='usuario'),
    url(r'^editar_usuario/(?P<usuario_id>\d+)/$', CadastroUsuario.as_view()),
    url(r'^desbloquear_usuario/', AdministrarUsuario.as_view()),
    url(r'^consulta_usuario/', ConsultaUsuario.as_view()),
    url(r'^visualizar_usuario/(?P<usuario_id>\d+)/$', VisualizarUsuario.as_view()),
    url(r'^liberar_usuario/(?P<usuario_verificacao>\w+)/$', LiberarUsuario.as_view()),
    url(r'^bloquear_usuario/(?P<usuario_verificacao>\w+)/$', BloquearUsuario.as_view()),
    url(r'^adm_on/(?P<usuario_verificacao>\w+)/$', AdmOn.as_view()),
    url(r'^adm_off/(?P<usuario_verificacao>\w+)/$', AdmOff.as_view()),

    url(r'^horario/', CadastroHorario.as_view(), name='horario'),
    url(r'^excluir_horario/(?P<horario_id>\d+)/$', ExcluirHorario.as_view()),    
    url(r'^editar_horario/(?P<horario_id>\d+)/$', CadastroHorario.as_view()),
    url(r'^hora_invalida/', hora_invalida),
    url(r'^apresentar_horarios/', ApresentarHorarios.as_view()),

    url(r'^curso/', CadastroCurso.as_view()),
    url(r'^editar_curso/(?P<curso_id>\d+)/$', CadastroCurso.as_view()),
    url(r'^consulta_curso/', ConsultaCurso.as_view()),
    url(r'^visualizar_curso/(?P<curso_id>\d+)/$', VisualizarCurso.as_view()),

    url(r'^projeto/', CadastroProjeto.as_view()),
    url(r'^editar_projeto/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),
    url(r'^consulta_projeto/', ConsultaProjeto.as_view()),
    url(r'^visualizar_projeto/(?P<projeto_id>\d+)/$', VisualizarProjeto.as_view()),
    url(r'^add_membro/(?P<projeto_id>\d+)/$', CadastroProjeto.as_view()),
    url(r'^editar_membro/(?P<projeto_id>\d+)/$', AddMembro.as_view()),
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
    url(r'^visualizar_edital/(?P<edital_id>\d+)/$', VisualizarEdital.as_view(), name='visualizar_edital'),
    
    url(r'^parceiro/', CadastroParceiro.as_view()),
    url(r'^editar_parceiro/(?P<parceiro_id>\d+)/$', CadastroParceiro.as_view()),
    url(r'^consulta_parceiro/', ConsultaParceiro.as_view()),
    url(r'^visualizar_parceiro/(?P<parceiro_id>\d+)/$', VisualizarParceiro.as_view()),

    url(r'^bolsa/$', CadastroBolsa.as_view(), name='cadastrar_bolsa'),
    url(r'^editar_bolsa/(?P<bolsa_id>\d+)/(?P<edital_id>\d+)/$', CadastroBolsa.as_view(), name='editar_bolsa'),
    url(r'^bolsa/edital/(?P<edital_id>\d+)/$', CadastroBolsa.as_view(), name='bolsa_por_edital'),

    url(r'^consulta_bolsa/', ConsultaBolsa.as_view()),
    url(r'^editar_bolsa/(?P<bolsa_id>\d+)/(?P<edital_id>\d+)/$', CadastroBolsa.as_view(), name='editar_bolsa'),
    url(r'^bolsa/edital/(?P<edital_id>\d+)/$', CadastroBolsa.as_view(), name='bolsa_por_edital'),
    url(r'^consulta_bolsa/', ConsultaBolsa.as_view(), name='consultar_bolsa'),
    url(r'^visualizar_bolsa/(?P<bolsa_id>\d+)/$', VisualizarBolsa.as_view()),

    url(r'^vinculo/', CadastroVinculo.as_view()),
    url(r'^vincular_bolsa/(?P<bolsa_id>\d+)/$', CadastroVinculoBolsa.as_view()),
    url(r'^editar_vinculo/(?P<vinculo_id>\d+)$', CadastroVinculo.as_view(), name='editar_vinculo'),

    url(r'^cadastrar_pagamento/$', CadastroPagamento.as_view(), name='cadastrar_pagamento'),
    url(r'^editar_pagamento/(?P<pagamento_id>\d+)/$', CadastroPagamento.as_view(), name='editar_pagamento'),
    url(r'^consulta_pagamento/$', ConsultaPagamento.as_view(), name='consultar_pagamento'),

    url(r'^log_cadastro/', LogCadastro.as_view()),
    url(r'^cadastros/', cadastros),

    url(r'^teste/$', verifica(), name='teste')



]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
