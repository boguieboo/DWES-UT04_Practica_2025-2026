# tareas/forms.py
from django import forms
from .models import Alumno, Profesor, Tarea
from django.utils import timezone

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'email', 'telefono']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@fpvirtualaragon.es'):
            raise forms.ValidationError("El email debe terminar en @fpvirtualaragon.es")
        return email


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'email', 'telefono']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@fpvirtualaragon.es'):
            raise forms.ValidationError("El email debe terminar en @fpvirtualaragon.es")
        return email



class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'tipo', 'evaluable', 'profesor_evaluador', 'alumnos']
        widgets = {
            'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}), # Selector de fecha y hora
            'tipo': forms.Select(), # Desplegable para tipo de tarea
            'alumnos': forms.CheckboxSelectMultiple(),  # Para selección múltiple de alumnos
        }

    # Validación: fecha de entrega > ahora
    def clean_fecha_entrega(self):
        fecha = self.cleaned_data['fecha_entrega']
        if fecha < timezone.now():
            raise forms.ValidationError("La fecha de entrega debe ser posterior a la fecha actual.")
        return fecha
