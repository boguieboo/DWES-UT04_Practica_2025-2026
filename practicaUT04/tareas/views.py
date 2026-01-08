# tareas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Alumno, Profesor

# from django.http import HttpResponse
# Vista para mostrar detalles de un alumno
def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    return render(request, 'tareas/detalle_alumno.html', {'alumno': alumno})

# Vista para mostrar detalles de un profesor
def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'tareas/detalle_profesor.html', {'profesor': profesor})


