from django.urls import path
from . import views

urlpatterns = [
    path('alumno/<uuid:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('profesor/<uuid:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
]
