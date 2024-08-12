from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from . import views, views_chat, views_admin, views_alumnos, views_profesores, views_materia, views_calificaciones, views_informes, views_graficos_barra, views_graficos_torta, views_login

urlpatterns = [
    path('', views.index, name='inicio'),
    path('adminred/', views_admin.index),
    path('chat/', views_chat.index),
    path('alumnos/', views_alumnos.index),
    path('alumnos/new/', views_alumnos.guardar_alumnos),
    path('alumnos/delete/', views_alumnos.eliminar_alumno),
    path('alumnos/editar/', views_alumnos.editar_alumno),
    path('alumnos/guardar/', views_alumnos.guardar_edit),
    path('profesores/', views_profesores.index),
    path('profesores/new/', views_profesores.guardar_profesores),
    path('profesores/delete/', views_profesores.eliminar_profesores),
    path('profesores/editar/', views_profesores.editar_profesores),
    path('profesores/guardar/', views_profesores.guardar_edit),
    path('profesores/importar_profesores/', views_profesores.importar_profesores_view, name='importar_profesores'),
    path('materias/', views_materia.index),
    path('materias/new/', views_materia.guardar_materia),
    path('materias/delete/', views_materia.eliminar_materia),
    path('materias/editar/', views_materia.editar_materia),
    path('materias/guardar/', views_materia.guardar_edit),
    path('calificaciones/', views_calificaciones.index),
   
    path('calificaciones/new/', views_calificaciones.guardar_calificaciones),
    path('calificaciones/delete/', views_calificaciones.eliminar_calificaciones),
    path('calificaciones/editar/', views_calificaciones.editar_calificaciones),
    path('calificaciones/guardar/', views_calificaciones.guardar_edit),
    path('informes/', views_informes.index),
    path('informes/generar/', views_informes.generar_informe),
    path('graficos/', views_graficos_barra.index, name='index'),
    path('alumnos/importar/', views_alumnos.importar_alumnos_view, name='importar_alumnos'),
    path('alumnos/exportar/', views_alumnos.exportar_alumnos, name='exportar_alumnos'),
    path('materias/importar_materias/', views_materia.importar_materias_view, name='importar_materias'),
    path('calificaciones/importar_calificaciones/', views_calificaciones.importar_calificaciones_view, name='importar_calificaciones'),
    re_path(r'^graficos/materia/(?P<materia_nombre>.+)/$', views_graficos_barra.grafico_materia, name='grafico_materia'),
    path('graficos/materias_por_curso/<int:curso_anio>/', views_graficos_barra.materias_por_curso, name='materias_por_curso'),
    path('graficos/grafico_torta/', views_graficos_torta.grafico_torta, name='grafico_torta'),
    path('graficos/torta/<int:materia_id>/', views_graficos_torta.grafico_torta_materia, name='grafico_torta_materia'),
    path('iniciar_sesion/', views_login.entrar, name='iniciar_sesion'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('calificaciones/mostrar/<int:curso>/', views_calificaciones.mostrar_calificaciones),
    # MDO MDO MDO
    path('alumnos/mostrar/<int:curso>/', views_alumnos.mostrar_alumnos)

    # MDO MDO MDO 
]
