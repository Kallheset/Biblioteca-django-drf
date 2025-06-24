# Biblioteca Django DRF

Sistema de gestión de biblioteca con Django y Django REST Framework.

## Características principales
- Gestión de libros, autores, usuarios y préstamos
- API RESTful documentada
- Panel de administración
- Almacenamiento de archivos y avatares en Cloudinary

## Requisitos
- Python 3.11+
- Docker y Docker Compose
- Cuenta en Cloudinary

## Instalación rápida
1. Clona el repositorio:
   ```bash
   git clone <URL-o-tu-fork>
   cd Biblioteca-django-drf-main
   ```
2. Copia el archivo `.env.dev` como `.env` y completa tus variables (Cloudinary, DB, etc).
3. Construye y levanta los servicios:
   ```bash
   docker-compose up --build
   ```
4. Aplica migraciones y crea un superusuario:
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

## Acceso rápido
- App web: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Documentación API: http://localhost:8000/api/schema/swagger-ui/

## Notas
- Los archivos subidos (avatares, portadas) se almacenan en Cloudinary.
- Para desarrollo local, la base de datos se ejecuta en MySQL dentro de Docker.
- Las variables de entorno críticas están en `.env.dev`.

---

Para dudas técnicas, revisa el código fuente o contacta al responsable del repositorio.
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret
```

## Desarrollo Local

1. Iniciar los contenedores:
```bash
docker-compose up
```

2. Crear superusuario:
```bash
docker-compose exec web python manage.py createsuperuser
```

3. Acceder a la aplicación:
- Panel de administración: http://localhost:8000/gestor-biblioteca/
- API Documentation: http://localhost:8000/api/docs/

## Estructura del Proyecto

```
biblioteca-backend/
├── apps/
│   ├── libros/          # Aplicación para gestión de libros
│   ├── prestamos/       # Aplicación para gestión de préstamos
│   └── autores/         # Aplicación para gestión de autores
├── biblioteca/          # Configuración principal del proyecto
├── templates/           # Plantillas HTML
├── static/             # Archivos estáticos
├── Dockerfile          # Configuración de Docker
├── docker-compose.yml  # Configuración de Docker Compose
└── requirements.txt    # Dependencias del proyecto
```

## API Endpoints

- `/api/libros/` - Gestión de libros
- `/api/categorias/` - Gestión de categorías
- `/api/prestamos/` - Gestión de préstamos
- `/api/docs/` - Documentación de la API (Swagger)
- `/api/redoc/` - Documentación alternativa (ReDoc)

## Seguridad

- Límite de intentos de inicio de sesión (5 intentos)
- URLs del admin personalizadas
- Autenticación requerida para la API
- Protección CSRF
- Variables de entorno para datos sensibles

## Despliegue

El proyecto está configurado para ser desplegado en Render. Los archivos de configuración incluyen:

- `Dockerfile` para la construcción de la imagen
- `docker-compose.yml` para la orquestación de contenedores
- `start.sh` para la inicialización del servicio









