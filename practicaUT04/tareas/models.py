from django.db import models
import uuid

# Modelo Alumno
class Alumno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


