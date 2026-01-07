from django.db import models
from django.contrib.auth.models import User
import uuid

# Modelo Alumno
class Alumno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

     # Relación 1:1 con el usuario que inicia sesión
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alumno")

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# Modelo Profesor
class Profesor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Relación 1:1 con el usuario que inicia sesión
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesor")

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# Modelo Tarea
class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField()

    TIPO_TAREA = [('INDIVIDUAL', 'Individual'), ('GRUPAL', 'Grupal')]
    tipo = models.CharField(max_length=10, choices=TIPO_TAREA, default='INDIVIDUAL')

    evaluable = models.BooleanField(default=False)

    profesor_evaluador = models.ForeignKey(
        Profesor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="tareas_evaluadas"
    )

    alumnos = models.ManyToManyField(Alumno, blank=True, related_name="tareas_participa")

    ESTADO = [('PENDIENTE', 'Pendiente'), ('ENTREGADA', 'Entregada'), ('CALIFICADA', 'Calificada')]
    estado = models.CharField(max_length=10, choices=ESTADO, default='PENDIENTE')

    creador_alumno = models.ForeignKey(
        Alumno, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="tareas_creadas"
    )

    creador_profesor = models.ForeignKey(
        Profesor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="tareas_creadas"
    )

    def __str__(self):
        return self.titulo




