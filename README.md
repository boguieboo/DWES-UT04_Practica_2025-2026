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
* [] id
* []nombre 
* []apellidos 
* []email
* []telefono 



## Modelo: Tarea
* [] ID
* [] Título
* [] Descripción
* [] Fecha de creación
* [] Fecha de entrega
* [] Creador
* [] Tipo de tarea: individual, grupal
* [] Evaluable
* [] Profesor evaluador
* [] Alumnos participantes
* [] Estado de la tarea









* [x] IBAN (opcional, sólo si quiere domiciliación bancaria).
* [x] Fecha de alta (auto).
* Info tutor si es menor: DNI tutor, nombre tutor, apellidos tutor y teléfono.

## Modelo: Dirección
Modificamos la primera versión para añadir un modelo con la dirección:
* Dirección con:
    * [x] calle
    * [x] número
    * [x] piso / puerta / extras (texto libre tipo "2ºB esc. izquierda")
    * [x] código postal
    * [x] ciudad (localidad)
    * [x] provincia
    * [x] país

## Modelo: Pago
    * [X] Creado el modelo con los pagos de las cuotas

## Vistas: Socio
* [X] Mostrar el listado de todos los socios (sólo se muestra DNI, nombre y apellidos)
* [X] Mostrar el detalle de un socio 

## Tareas a realizar

* [x] Actualizar el modelo de socios añadiendo tutores y roles
* [ ] Genera vistas en dos formatos: usando el modelo completo y solo con parte de él
* [X] Configurar la aplicación para utilizar Postgres ✓
* [ ] Implementar herencia entre los tipos de socios 
* [X] Formularios para crear un socio y validación de datos ✓
* [ ]  

