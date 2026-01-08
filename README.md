# DWES-UT04_Practica_2025-2026
Práctica UT04 Persistencia de datos

En esta práctica deberas desarrollar una aplicación web para la gestión de tareas en un entorno educativo 
que permita a profesores crear y administrar diferentes tipos de tareas, y a alumnos visualizarlas y completarlas.

* El sistema distinguirá entre tres tipos de tareas: individuales, grupales y evaluables,

* Las tareas tendrán con diferentes fórmulas para completarse según el rol de usuario: alumno o profesor.

* Como alumno podré crear tareas de los distintos tipos existentes.

* Como alumno podré validar la finalización de una tarea, que no requiera evaluación del profesor.

* Como profesor podré validar la finalización de tareas que lo requieran.


## Listado de elementos a implementar
## Modelo: Alumno
* [x] id
* [x] nombre 
* [x] apellidos 
* [x] email
* [x] telefono 

## Modelo: Profesor
* [x] id
* [x] nombre 
* [x] apellidos 
* [x] email
* [x] telefono 


## Modelo: Tarea
* [x] ID
* [x] Título
* [x] Descripción
* [x] Fecha de creación
* [x] Fecha de entrega
* [x] Tipo de tarea: individual, grupal
* [x] Evaluable
* [x] Profesor evaluador
* [x] Alumnos participantes
* [x] Estado de la tarea
* [x] Creador

He usado un modelo único de tarea para representar los tipos de tareas individual, grupal y evaluable.
Individual o grupal con desplegable.
Si es Evaluable con un check
Y si requiere la evaluación de un profesor con un desplegable en el que poner el nombre del profe.

## Tareas a realizar
Vistas
* [X] Vista en la que un alumno/profesor pueda ver sus datos.
* [X] Vista con el listado de todo el alumnado/profesorado.
* [X] Vista en la que un alumno puede ver todas las tareas que ha creado o colabora.
* [X] Vista en la que un profesor puede ver todas las tareas que requieren su validación.

Formularios
* [X] Formulario para el alta del alumnado/profesorado.
* [X] Formulario de creación de una tarea individual (puede necesitar o no evaluación de un profesor)
* [X] Formulario de creación de una tarea grupal (puede necesitar o no evaluación de un profesor)
Nota: está en un mismo formulario de tarea donde seleccionas si es grupal o individual y si requiere
evaluación de un profesor

## DIAGRAMA DE TABLAS CON RELACIONES
Mi proyecto tiene tres entidades principales:
* Alumno: con los datos personales y con las tareas que ha creado / que participa.
    Un alumno puede crear varias tareas y también puede participar en múltiples tareas grupales.
* Profesor: con los datos personales y con las tareas que puede crear / evaluar.
    Un profesor puede crear tareas y, además, puede actuar como evaluador de las mismas.
* Tarea: elemento principal del sistema. Se relaciona con alumno y profesor.

```mermaid
erDiagram
    ALUMNO {
        UUID id PK
        string nombre
        string apellidos
        string email
        string telefono
    }

    PROFESOR {
        UUID id PK
        string nombre
        string apellidos
        string email
        string telefono
    }

    TAREA {
        UUID id PK
        string titulo
        text descripcion
        datetime fecha_creacion
        datetime fecha_entrega
        string tipo
        boolean evaluable
        string estado
    }

    %% Relaciones

    ALUMNO ||--o{ TAREA : "crea"
    PROFESOR ||--o{ TAREA : "crea"
    PROFESOR ||--o{ TAREA : "evalúa"
    ALUMNO }o--o{ TAREA : "participa"
  

