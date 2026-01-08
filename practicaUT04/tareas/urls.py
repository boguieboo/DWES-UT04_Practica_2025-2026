from django.urls import path
from . import views

urlpatterns = [
    path('alumno/<uuid:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('profesor/<uuid:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
    path('alta_alumno/', views.alta_alumno, name='alta_alumno'),
    path('alta_profesor/', views.alta_profesor, name='alta_profesor'),
    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('listar_profesores/', views.listar_profesores, name='listar_profesores'),
]
