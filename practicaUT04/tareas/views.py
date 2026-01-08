# tareas/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Alumno, Profesor, Tarea
from .forms import AlumnoForm, ProfesorForm, TareaForm


# from django.http import HttpResponse
# Vista para mostrar detalles de un alumno
def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    return render(request, 'tareas/detalle_alumno.html', {'alumno': alumno})

# Vista para mostrar detalles de un profesor
def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'tareas/detalle_profesor.html', {'profesor': profesor})

# Vista para dar de alta un alumno
def alta_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Alumno dado de alta correctamente.")
    else:
        form = AlumnoForm()
    return render(request, 'tareas/alta_alumno.html', {'form': form})

# Vista para dar de alta un profesor
def alta_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Profesor dado de alta correctamente.")
    else:
        form = ProfesorForm()
    return render(request, 'tareas/alta_profesor.html', {'form': form})

# Vista para listar todos los alumnos
def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'tareas/listar_alumnos.html', {'alumnos': alumnos})

# Vista para listar todos los profesores
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'tareas/listar_profesores.html', {'profesores': profesores}) 

# Vista para crear una tarea
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tarea creada correctamente.")
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

# Vista para listar todas las tareas
def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/listar_tareas.html', {'tareas': tareas}) 

# Vista detalle de una tarea
def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})   

     
