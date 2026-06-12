# 🏠 HomeFix

## 📌 Descripción del Proyecto

HomeFix es una plataforma web diseñada para conectar empleadores con trabajadores especializados en servicios domésticos y mantenimiento del hogar. La aplicación permite que ambas partes interactúen de forma sencilla para llegar a acuerdos sobre trabajos como plomería, electricidad, pintura, albañilería, instalación de cámaras de seguridad, limpieza, jardinería y otros servicios relacionados.

El objetivo principal es facilitar la búsqueda y contratación de trabajadores confiables mediante una plataforma organizada, intuitiva y accesible.

---

## 🎯 Objetivo General

Desarrollar una aplicación web que permita conectar empleadores y trabajadores de servicios domésticos, facilitando la gestión de perfiles, la comunicación y la contratación de servicios para el hogar.

---

## 👥 Roles del Sistema

### Empleador
- Crear una cuenta.
- Iniciar sesión.
- Buscar trabajadores.
- Visualizar perfiles.
- Contactar trabajadores.
- Gestionar solicitudes de servicio.

### Empleado
- Crear una cuenta.
- Iniciar sesión.
- Crear y editar su perfil.
- Publicar información sobre sus habilidades.
- Recibir solicitudes de trabajo.
- Gestionar su información personal.

---

## 🚀 Funcionalidades Implementadas

### 🔐 Autenticación
- Registro de usuarios.
- Inicio de sesión.
- Validación de datos.

### 👤 Gestión de Perfil
- Visualización de información personal.
- Edición de datos del usuario.
- Actualización de perfil.

### 🎨 Interfaz de Usuario
- Diseño responsivo.
- Navegación intuitiva.
- Dashboard principal.
- Perfil de usuario.

### ⚙️ Backend
- Conexión con base de datos.
- Gestión de usuarios.
- API desarrollada en Python.

---

## 🏗️ Arquitectura del Proyecto

```text
HomeFix/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── usuario.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── perfil1.html
│
├── Css/
│   └── style.css
│
├── perfil.html
├── perfil1.html
└── README.md
```

---

## 🛠️ Tecnologías Utilizadas

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI

### Base de Datos
- PostgreSQL

### Control de Versiones
- Git
- GitHub

---

## 📚 Programación Orientada a Objetos (POO)

### Pilar Implementado: Encapsulación

Para cumplir con los requisitos del proyecto se implementó el pilar de **Encapsulación** mediante la clase `Usuario`.

La encapsulación consiste en proteger los datos internos de una clase, permitiendo el acceso únicamente a través de métodos controlados.

### Clase Usuario

Archivo:

```text
backend/usuario.py
```

### Atributos Privados

```python
self.__nombre
self.__correo
self.__telefono
```

### Métodos Getter

```python
get_nombre()
get_correo()
get_telefono()
```

### Métodos Setter

```python
set_nombre()
set_correo()
set_telefono()
```

### Beneficios

- Protección de datos.
- Control de acceso a la información.
- Mayor seguridad y mantenimiento del código.
- Aplicación de buenas prácticas de Programación Orientada a Objetos.

---

## 📋 Ejemplo de Uso

```python
from usuario import Usuario

usuario = Usuario(
    "Ronald Verano",
    "ronald@gmail.com",
    "3001234567"
)

print(usuario.mostrar_datos())

usuario.set_nombre("Ronald Sosa")

print(usuario.mostrar_datos())
```

---

## ⚡ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ronaldsvs17-jpg/HomeFix.1.git
```

### 2. Entrar al proyecto

```bash
cd HomeFix.1
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r backend/requirements.txt
```

### 6. Ejecutar el servidor

```bash
uvicorn app:app --reload
```

---

## 📈 Mejoras Futuras

- Sistema de mensajería en tiempo real.
- Calificación de trabajadores.
- Historial de servicios.
- Sistema de pagos en línea.
- Notificaciones automáticas.
- Panel administrativo.

---

## 👨‍💻 Autores

**Ronald Verano Sosa**
**Johan Olaya**
Proyecto académico desarrollado para la asignatura de Programación Orientada a Objetos y Desarrollo Web.

---

## 📄 Licencia

Este proyecto tiene fines educativos y académicos.
