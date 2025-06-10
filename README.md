# Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca desarrollado con Django y Django REST Framework, que permite administrar libros, préstamos y usuarios.

## Características

- Gestión de libros y categorías
- Sistema de préstamos
- API REST completa
- Panel de administración personalizado
- Autenticación y autorización
- Documentación de API con Swagger/ReDoc
- Límite de intentos de inicio de sesión
- Almacenamiento de archivos en Cloudinary

## Requisitos

- Python 3.11+
- Docker y Docker Compose
- Cuenta en Cloudinary (para almacenamiento de archivos)

## Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone https://github.com/Kallheset/Biblioteca-django-drf.git
cd biblioteca-backend
```

2. Crear archivo `.env` con las siguientes variables:
```env
DEBUG=True
SECRET_KEY=tu_clave_secreta
DB_ENGINE=django.db.backends.mysql
DB_NAME=biblioteca_db
DB_USER=biblioteca_user
DB_PASSWORD=biblioteca_pass
DB_HOST=db
DB_PORT=3306
CLOUDINARY_CLOUD_NAME=tu_cloud_name
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

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request







