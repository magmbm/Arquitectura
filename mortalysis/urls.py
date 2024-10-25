from django.urls import path
from . import views

urlpatterns= [
    path("analisis", views.analisis, name="analisis"),
    path("index", views.index, name="index"),
    path("errores_mortales", views.listar_errores_mortales, name="errores_mortales"),
    path("errores_mortales/agregar", views.registrar_error_mortal, name="registrar_error_mortal"),
    path("errores_mortales/editar/<int:pk>", views.editar_error_mortal, name="editar_error_mortal"),
    path("errores_mortales/eliminar/<int:pk>", views.eliminar_error_mortal, name="eliminar_error_mortal"),
    path("pacientes", views.listar_pacientes, name="pacientes"),
    path("pacientes/agregar", views.registrar_paciente, name="agregar_paciente"),
    path("pacientes/editar/<int:pk>", views.editar_paciente, name="editar_paciente"),
    path("pacientes/eliminar/<int:pk>", views.eliminar_paciente, name="eliminar_paciente"),
    path('defunciones/', views.listar_defunciones, name='defunciones'),
    path('defunciones/agregar', views.registrar_defuncion, name='registrar_defuncion'),
    path('defunciones/editar/<int:pk>', views.editar_defuncion, name='editar_defuncion'),
    path('defunciones/eliminar/<int:pk>', views.eliminar_defuncion, name='eliminar_defuncion'),
    path('reporte', views.reporte, name="reporte")
]