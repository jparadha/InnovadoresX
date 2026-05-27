# InnovadoresX – Sistema de Registro Escolar

Repositorio desarrollado para la evaluación práctica de Programación en Python utilizando interfaces gráficas con Tkinter.

## Descripción

InnovadoresX es una aplicación de escritorio desarrollada en Python utilizando la librería Tkinter. El sistema permite registrar información de estudiantes mediante una interfaz gráfica amigable y organizada.

La aplicación fue diseñada con el objetivo de aplicar distintos widgets de Tkinter, validación de datos y manejo de formularios dentro de un entorno visual.

---

## Funcionalidades del sistema

El programa permite:

* Registrar información de estudiantes.
* Ingresar datos personales y académicos.
* Seleccionar estado de inscripción.
* Escoger materias optativas.
* Agregar comentarios adicionales.
* Seleccionar nivel escolar mediante menú desplegable.
* Validar campos obligatorios.
* Limpiar automáticamente el formulario.

---

## Tecnologías utilizadas

* Python 3
* Tkinter
* Visual Studio Code

---

## Widgets utilizados en Tkinter

La interfaz incorpora distintos componentes gráficos:

| Widget             | Función                            |
| ------------------ | ---------------------------------- |
| Frame / LabelFrame | Organizar secciones de la interfaz |
| Label              | Mostrar textos descriptivos        |
| Entry              | Capturar información del usuario   |
| Text               | Ingresar comentarios extensos      |
| Button             | Ejecutar acciones                  |
| Radiobutton        | Seleccionar estado de inscripción  |
| Checkbutton        | Elegir materias optativas          |
| OptionMenu         | Seleccionar nivel escolar          |

---

## Estructura de la interfaz

La interfaz fue organizada mediante distintos Frames:

* Datos personales
* Detalles académicos
* Estado de inscripción
* Materias optativas
* Comentarios adicionales
* Nivel escolar
* Botones de acción

Esto permite mantener una distribución clara y ordenada para el usuario.

---

## Validaciones implementadas

El sistema incorpora validaciones básicas para mejorar la integridad de los datos ingresados.

Ejemplo:

* El nombre del estudiante es obligatorio.
* Se muestran mensajes de advertencia utilizando `messagebox`.

---

## Ejecución del programa

1. Instalar Python 3.
2. Abrir el proyecto en Visual Studio Code.
3. Ejecutar el archivo principal:

```bash
python innovadoresx.py
```

---

## Ejemplo de funcionamiento

El usuario puede:

* Completar el formulario.
* Seleccionar materias.
* Registrar estudiantes.
* Visualizar la información en la terminal de Visual Studio Code.
* Limpiar todos los campos del formulario.

---

## Autor

Desarrollado como proyecto académico utilizando Python y Tkinter.
