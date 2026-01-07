from django.db import models
from django.contrib.auth.models import User
import uuid

# Modelo Alumno
class Alumno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

     # Relación 1:1 con el usuario que inicia sesión
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alumno")

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesor")
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


