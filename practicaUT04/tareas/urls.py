from django.urls import path
from . import views

urlpatterns = [
    path('alumno/<uuid:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('profesor/<uuid:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
    path('alta_alumno/', views.alta_alumno, name='alta_alumno'),
    path('alta_profesor/', views.alta_profesor, name='alta_profesor'),
    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('listar_profesores/', views.listar_profesores, name='listar_profesores'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('listar_tareas/', views.listar_tareas, name='listar_tareas'),
    path('tarea/<uuid:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('alumno/<uuid:alumno_id>/tareas/', views.tareas_del_alumno, name='tareas_alumno'),
    path('profesor/<uuid:profesor_id>/tareas/', views.tareas_a_evaluar, name='tareas_profesor'),
]
