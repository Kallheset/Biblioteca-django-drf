# Sistema de Biblioteca

Sistema de gestión de biblioteca desarrollado con Django y Django REST Framework.

## Características

- Gestión de libros, autores y categorías
- Sistema de préstamos de libros
- API REST para integración con otros sistemas
- Autenticación de usuarios
- Interfaz web responsive
- Documentación interactiva de la API (Swagger UI y Redoc)

## Requisitos

- Python 3.8+
- MySQL 5.7+
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd biblioteca-backend
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
DB_NAME=biblioteca
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
```

5. Aplicar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## Uso

### Interfaz Web

- URL base: `http://localhost:8000/`
- Panel de administración: `http://localhost:8000/admin/`
- Documentación Swagger UI: `http://localhost:8000/api/docs/`
- Documentación Redoc: `http://localhost:8000/api/redoc/`
- Esquema OpenAPI (JSON): `http://localhost:8000/api/schema/`

### Flujo de la Aplicación

1. **Acceso Público**:
   - Ver lista de libros disponibles
   - Buscar libros por título, autor o categoría
   - Ver detalles de los libros

2. **Acceso Autenticado**:
   - Iniciar sesión: `/login/`
   - Registro de usuarios: `/registro/`
   - Gestión de préstamos: `/prestamos/`
   - Devolución de libros

3. **Funcionalidades por Usuario**:
   - Ver préstamos activos
   - Ver historial de préstamos
   - Devolver libros
   - Solicitar nuevos préstamos

### API REST

La API está disponible en `/api/` y requiere autenticación de usuario (session auth o token según configuración).

Endpoints principales:
- `/api/libros/`: Gestión de libros
- `/api/categorias/`: Gestión de categorías
- `/api/prestamos/`: Gestión de préstamos

La documentación interactiva y el esquema OpenAPI están disponibles en:
- Swagger UI: `/api/docs/`
- Redoc: `/api/redoc/`
- OpenAPI JSON: `/api/schema/`


### Estructura del Proyecto

```
biblioteca-backend/
├── apps/
│   ├── autores/
│   ├── libros/
│   └── prestamos/
├── biblioteca/
├── templates/
├── static/
└── media/
```

## Base de Datos

Este proyecto utiliza MySQL como sistema de gestión de base de datos. Debes crear una base de datos vacía llamada `biblioteca` (o el nombre que definas en tu archivo `.env`)

Asegúrate de tener un usuario y contraseña válidos para conectarte a MySQL. Puedes crear la base de datos ejecutando:

```sql
CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

El archivo `.env` debe contener los datos de conexión:

```
DB_NAME=biblioteca
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
```

Las migraciones de Django crearán automáticamente las tablas necesarias al ejecutar:

```bash
python manage.py migrate
```

### Comandos Útiles

- Crear migraciones: `python manage.py makemigrations`
- Aplicar migraciones: `python manage.py migrate`
- Crear superusuario: `python manage.py createsuperuser`





