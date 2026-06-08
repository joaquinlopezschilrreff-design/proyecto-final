# 📚 StudyMood

**Autor:** Joaco

## 📖 Descripción

StudyMood es una aplicación web desarrollada con Python, Flask y SQLite que ayuda a los estudiantes a organizar sus apuntes y resúmenes de forma sencilla.

El objetivo principal del proyecto es permitir que cada usuario tenga su propio espacio de estudio donde pueda guardar, editar, escuchar y descargar sus resúmenes organizados por materia.

---

## 🎯 Finalidad del proyecto

Este proyecto fue creado como práctica de programación y desarrollo web.

StudyMood busca facilitar la organización del estudio permitiendo:

* Guardar resúmenes por materia.
* Acceder a los apuntes desde una única plataforma.
* Escuchar los resúmenes mediante síntesis de voz.
* Descargar los resúmenes para utilizarlos fuera de la aplicación.
* Mantener la información organizada para cada usuario.

---

## ✨ Funciones y características

### 👤 Gestión de usuarios

* Registro de usuarios.
* Inicio de sesión.
* Cierre de sesión.
* Validación de contraseñas.
* Prevención de correos duplicados.
* Sesiones seguras para cada usuario.

### 📚 Organización por materias

Las materias disponibles son:

* Matemática
* Historia
* Biología
* Lengua
* Geografía
* Computación
* Arte
* Música

### 📝 Gestión de resúmenes

* Crear resúmenes.
* Editar resúmenes.
* Guardar información automáticamente en SQLite.
* Almacenar fecha de última modificación.

### 🔊 Síntesis de voz

* Lectura automática de resúmenes.
* Botón para detener la lectura.

### ⬇ Exportación

* Descarga de resúmenes en formato .txt.

### 📊 Información del usuario

* Cantidad de resúmenes guardados.
* Total de palabras escritas.
* Última materia modificada.

---

## 🛠️ Tecnologías utilizadas

* Python
* Flask
* SQLite
* HTML5
* CSS3
* JavaScript

---

## 📂 Estructura del proyecto

```text
proyecto-final/
│
├── main.py
├── usuarios.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── materias.html
│   └── materia.html
│
└── static/
    └── style.css
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/StudyMood.git
```

### 2. Entrar al proyecto

```bash
cd StudyMood
```

### 3. Instalar Flask

```bash
pip install flask
```

### 4. Ejecutar la aplicación

```bash
python main.py
```

### 5. Abrir en el navegador

```text
http://127.0.0.1:5000
```

---

## 💡 Uso del proyecto

1. Crear una cuenta.
2. Iniciar sesión.
3. Elegir una materia.
4. Escribir o editar un resumen.
5. Guardar los cambios.
6. Escuchar el resumen mediante voz.
7. Descargar el resumen en formato TXT.

---

## 💬 Comentarios y participación

Los usuarios pueden aportar sugerencias, reportar errores o proponer nuevas funciones mediante los comentarios y herramientas de GitHub.

Las ideas para futuras versiones incluyen:

* Más materias.
* Modo claro/oscuro.
* Exportación a PDF.
* Calendario de estudio.
* Recordatorios de tareas.

---

## 🏁 Conclusión

StudyMood es una herramienta educativa diseñada para ayudar a los estudiantes a organizar mejor sus apuntes y mejorar sus hábitos de estudio.

El proyecto permitió aplicar conocimientos de desarrollo web, bases de datos, programación en Python y diseño de interfaces, combinando diferentes tecnologías en una aplicación funcional y útil para estudiantes.
