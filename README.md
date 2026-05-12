# 📚 Sistema de Gestión de Biblioteca - Django REST Framework

> **Proyecto Full-Stack** desarrollado con Django 5.2 y Django REST Framework, demostrando arquitectura de software profesional, optimización de bases de datos, testing automatizado y despliegue en producción.

[![Django CI](https://github.com/Kallheset/Biblioteca-django-drf/actions/workflows/ci.yml/badge.svg)](https://github.com/Kallheset/Biblioteca-django-drf/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Django 5.2](https://img.shields.io/badge/django-5.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red.svg)](https://www.django-rest-framework.org/)

---

## 🎯 Descripción del Proyecto

Sistema completo de gestión bibliotecaria que permite administrar libros, autores, categorías y préstamos de usuarios. Implementa **mejores prácticas de desarrollo backend** incluyendo arquitectura en capas, optimización de consultas SQL, manejo avanzado de excepciones, testing automatizado y CI/CD con GitHub Actions.

**🔗 Demo en Vivo:** [biblioteca-django-drf.onrender.com](https://biblioteca-django-drf.onrender.com)

---

## 🚀 Habilidades Técnicas Demostradas

### 🏗️ **Arquitectura y Diseño**

- ✅ **Arquitectura en Capas**: Separación de responsabilidades con capa de servicios (`services.py`) para lógica de negocio
- ✅ **Manejo de Excepciones Personalizado**: Sistema robusto con `BusinessLogicError` y handlers globales
- ✅ **Patrones de Diseño**: Repository pattern, Service layer, Dependency Injection
- ✅ **Código Limpio**: Adherencia a PEP 8, type hints, documentación exhaustiva

### 🗄️ **Base de Datos y Optimización**

- ✅ **Optimización de Consultas**: Eliminación del problema N+1 con `select_related()` y `prefetch_related()`
- ✅ **Transacciones Atómicas**: Uso de `@transaction.atomic` para garantizar integridad de datos
- ✅ **Migraciones Complejas**: Gestión profesional de esquemas de base de datos
- ✅ **Soporte Multi-DB**: MySQL (producción) y SQLite (testing/desarrollo)

### 🔌 **API REST y Serialización**

- ✅ **Django REST Framework**: Endpoints completos con paginación, filtrado y búsqueda
- ✅ **Serializers Avanzados**: Validación personalizada, campos anidados, write-only fields
- ✅ **Autenticación JWT**: Implementación de tokens con `djangorestframework-simplejwt`
- ✅ **Documentación OpenAPI**: Integración con `drf-spectacular` para Swagger UI
- ✅ **Versionado de API**: Preparado para múltiples versiones de API

### 🧪 **Testing y Calidad de Código**

- ✅ **Testing Unitario**: Cobertura con pytest y pytest-django
- ✅ **Fixtures y Factories**: Datos de prueba reutilizables y mantenibles
- ✅ **CI/CD con GitHub Actions**: Ejecución automática de tests en cada push/PR
- ✅ **Cobertura de Código**: Reportes HTML con pytest-cov

### 🔐 **Seguridad**

- ✅ **Autenticación y Autorización**: Sistema completo con permisos personalizados
- ✅ **Headers de Seguridad**: HSTS, X-Frame-Options, Content-Type-Nosniff
- ✅ **Rate Limiting**: Throttling para prevenir abuso de API
- ✅ **CSRF Protection**: Protección contra ataques CSRF
- ✅ **Gestión de Secretos**: Variables de entorno con python-dotenv

### ☁️ **DevOps y Deployment**

- ✅ **Containerización**: Dockerfile y docker-compose para desarrollo local
- ✅ **Deployment en Render**: Configuración completa con `render.yaml`
- ✅ **Static Files**: Gestión con WhiteNoise para servir archivos estáticos
- ✅ **Media Files**: Integración con Cloudinary para almacenamiento en la nube
- ✅ **Scripts de Deploy**: Automatización con `build.sh` y creación de superusuario

### 🎨 **Frontend y UX**

- ✅ **Interfaz Premium**: Diseño moderno con glassmorphism y micro-animaciones
- ✅ **Dark Mode Nativo**: Sistema de temas con persistencia en localStorage
- ✅ **Responsive Design**: Adaptación perfecta a dispositivos móviles
- ✅ **Accesibilidad**: Contraste optimizado y navegación por teclado

---

## 🛠️ Stack Tecnológico

### **Backend**

- **Framework:** Django 5.2.1
- **API:** Django REST Framework 3.15.2
- **Base de Datos:** MySQL 8.0 (Producción) / SQLite (Testing)
- **Autenticación:** JWT con djangorestframework-simplejwt
- **Documentación:** drf-spectacular (OpenAPI/Swagger)

### **Testing & CI/CD**

- **Testing:** pytest, pytest-django, pytest-cov
- **CI/CD:** GitHub Actions
- **Linting:** flake8, black (preparado)

### **Deployment**

- **Servidor:** Gunicorn
- **Archivos Estáticos:** WhiteNoise
- **Media Storage:** Cloudinary
- **Hosting:** Render.com
- **Containerización:** Docker + Docker Compose

### **Librerías Adicionales**

- **Filtrado:** django-filter
- **CORS:** django-cors-headers
- **Variables de Entorno:** python-dotenv
- **Base de Datos:** mysqlclient, dj-database-url

---

## 📂 Estructura del Proyecto

```
Biblioteca-django-drf/
├── apps/
│   ├── autores/              # Gestión de autores
│   ├── common/               # Excepciones y utilidades compartidas
│   │   └── exceptions.py     # BusinessLogicError, handlers globales
│   ├── libros/               # Gestión de libros y categorías
│   │   ├── services.py       # Capa de servicios (lógica de negocio)
│   │   ├── serializers.py    # Serialización y validación
│   │   └── tests/            # Tests unitarios
│   ├── prestamos/            # Sistema de préstamos
│   │   ├── services.py       # Lógica de préstamos con validaciones
│   │   └── tests/            # Tests de servicios
│   └── usuarios/             # Gestión de usuarios y perfiles
│
├── biblioteca/               # Configuración del proyecto
│   ├── settings.py           # Configuración adaptativa (dev/prod)
│   └── urls.py               # Enrutamiento principal
│
├── static/                   # Archivos estáticos (CSS, JS)
│   └── css/
│       └── styles.css        # Sistema de diseño con variables CSS
│
├── templates/                # Templates HTML
│   ├── base.html             # Layout base con theme switcher
│   ├── libros.html           # Catálogo de libros
│   ├── prestamos.html        # Gestión de préstamos
│   └── usuarios/             # Perfiles y autenticación
│
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions para CI/CD
│
├── build.sh                  # Script de build para Render
├── create_superuser.py       # Creación automática de admin
├── docker-compose.yml        # Orquestación de contenedores
├── Dockerfile                # Imagen Docker
├── pytest.ini                # Configuración de pytest
├── render.yaml               # Configuración de Render
└── requirements.txt          # Dependencias del proyecto
```

---

## 🔥 Características Destacadas

### 🎯 **Optimización de Rendimiento**

- **Eliminación del problema N+1**: Todas las consultas optimizadas con `select_related()` y `prefetch_related()`
- **Índices de Base de Datos**: Campos clave indexados para búsquedas rápidas
- **Caching Ready**: Preparado para implementar Redis/Memcached
- **Paginación Eficiente**: Limitación de resultados para reducir carga

### 🧩 **Arquitectura de Servicios**

```python
# Ejemplo: apps/prestamos/services.py
class PrestamoService:
    @staticmethod
    @transaction.atomic
    def crear_prestamo(usuario, libro, dias_prestamo=7):
        # Validación de disponibilidad
        if not libro.disponible or libro.stock <= 0:
            raise BusinessLogicError(f'El libro "{libro.titulo}" no está disponible.')
        
        # Validación de límite de préstamos
        prestamos_activos = Prestamo.objects.filter(
            usuario=usuario,
            fecha_devolucion__isnull=True
        ).count()
        
        if prestamos_activos >= MAX_LIBROS_POR_USUARIO:
            raise BusinessLogicError(f'El usuario ha alcanzado el límite de {MAX_LIBROS_POR_USUARIO} préstamos.')
        
        # Crear préstamo y actualizar stock
        prestamo = Prestamo.objects.create(...)
        libro.stock -= 1
        libro.disponible = libro.stock > 0
        libro.save()
        
        return prestamo
```

### 🔒 **Manejo de Excepciones Robusto**

```python
# apps/common/exceptions.py
class BusinessLogicError(Exception):
    """Excepción para errores de lógica de negocio"""
    pass

def biblioteca_exception_handler(exc, context):
    """Handler global para excepciones personalizadas"""
    if isinstance(exc, BusinessLogicError):
        return Response(
            {'error': str(exc)},
            status=status.HTTP_400_BAD_REQUEST
        )
    return exception_handler(exc, context)
```

### 🧪 **Testing Profesional**

```python
# apps/libros/tests/test_libro_services.py
@pytest.mark.django_db
class TestLibroService:
    def test_actualizar_stock_error_insuficiente(self, setup_data):
        libro = setup_data
        with pytest.raises(ValidationError):
            LibroService.actualizar_stock(libro, -10)
```

---

## 🚀 Instalación y Configuración

### **Requisitos Previos**

- Python 3.12+
- MySQL 8.0+ (o SQLite para desarrollo)
- Git

### **1. Clonar el Repositorio**

```bash
git clone https://github.com/Kallheset/Biblioteca-django-drf.git
cd Biblioteca-django-drf
```

### **2. Crear Entorno Virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3. Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### **4. Configurar Variables de Entorno**

Copia `.env.example` a `.env` y configura:

```env
SECRET_KEY=tu-secret-key-super-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de Datos (MySQL)
DB_ENGINE=django.db.backends.mysql
DB_NAME=biblioteca_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=127.0.0.1
DB_PORT=3306

# Cloudinary (opcional para imágenes)
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret
```

### **5. Aplicar Migraciones**

```bash
python manage.py migrate
```

### **6. Crear Superusuario**

```bash
python manage.py createsuperuser
```

### **7. Ejecutar Servidor de Desarrollo**

```bash
python manage.py runserver
```

Accede a:

- **Aplicación:** <http://127.0.0.1:8000/>
- **Admin:** <http://127.0.0.1:8000/admin/>
- **API:** <http://127.0.0.1:8000/api/>
- **Swagger UI:** <http://127.0.0.1:8000/api/schema/swagger-ui/>

---

## 🐳 Ejecución con Docker

### **Desarrollo Local**

```bash
docker-compose up --build
```

Esto levantará:

- **MySQL 8.0** en puerto 3307
- **Django App** en puerto 8000

### **Acceder al Contenedor**

```bash
docker exec -it biblioteca_app bash
```

---

## 🧪 Testing

### **Ejecutar Todos los Tests**

```bash
pytest
```

### **Con Cobertura de Código**

```bash
pytest --cov=apps --cov-report=html
```

### **Tests Específicos**

```bash
pytest apps/libros/tests/
pytest apps/prestamos/tests/
```

### **CI/CD Automático**

Los tests se ejecutan automáticamente en cada push mediante GitHub Actions. Ver resultados en la pestaña [Actions](https://github.com/Kallheset/Biblioteca-django-drf/actions).

---

## 📡 API Endpoints

### **Autenticación**

```
POST   /api/token/          # Obtener token JWT
POST   /api/token/refresh/  # Refrescar token
```

### **Libros**

```
GET    /api/libros/                    # Listar libros (paginado)
POST   /api/libros/                    # Crear libro
GET    /api/libros/{id}/               # Detalle de libro
PUT    /api/libros/{id}/               # Actualizar libro
DELETE /api/libros/{id}/               # Eliminar libro
GET    /api/libros/?search=titulo      # Búsqueda
GET    /api/libros/?categoria=1        # Filtrar por categoría
```

### **Préstamos**

```
GET    /api/prestamos/                 # Listar préstamos del usuario
POST   /api/prestamos/                 # Crear préstamo
POST   /api/prestamos/{id}/devolver/   # Devolver libro
```

### **Documentación Interactiva**

```
GET    /api/schema/swagger-ui/         # Swagger UI
GET    /api/schema/redoc/              # ReDoc
GET    /api/schema/                    # OpenAPI Schema (JSON)
```

---

## 🌐 Deployment en Render

### **Despliegue Automático**

1. Conecta tu repositorio de GitHub a Render
2. Configura las variables de entorno en el Dashboard
3. Render ejecutará automáticamente `build.sh`
4. El superusuario se creará automáticamente si configuras:
   - `DJANGO_SUPERUSER_USERNAME`
   - `DJANGO_SUPERUSER_EMAIL`
   - `DJANGO_SUPERUSER_PASSWORD`

### **Variables de Entorno Requeridas en Render**

```
SECRET_KEY
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com
DB_ENGINE=django.db.backends.mysql
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=3306
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
```

---

## � Métricas del Proyecto

- **Líneas de Código:** ~3,500+ (Python)
- **Tests Unitarios:** 8 tests (100% passing)
- **Cobertura de Código:** ~75%
- **Endpoints API:** 15+
- **Modelos de Datos:** 6 (Libro, Autor, Categoría, Préstamo, Usuario, Perfil)
- **Tiempo de Build:** ~2 minutos
- **Tiempo de Deploy:** ~3 minutos

---

## 🎓 Aprendizajes y Mejores Prácticas

Este proyecto demuestra:

1. ✅ **Separación de Responsabilidades**: Arquitectura en capas con servicios dedicados
2. ✅ **Optimización de Consultas**: Eliminación del problema N+1
3. ✅ **Testing Riguroso**: Cobertura de casos edge y validaciones de negocio
4. ✅ **Seguridad First**: Implementación de mejores prácticas de seguridad
5. ✅ **CI/CD Profesional**: Automatización completa del pipeline
6. ✅ **Documentación Exhaustiva**: Código autodocumentado y README completo
7. ✅ **Deployment Real**: Aplicación desplegada en producción

---

## � Roadmap y Mejoras Futuras

- [ ] Implementar sistema de notificaciones (email/SMS)
- [ ] Agregar sistema de reseñas y calificaciones
- [ ] Implementar caché con Redis
- [ ] Agregar búsqueda full-text con Elasticsearch
- [ ] Implementar sistema de reservas
- [ ] Agregar dashboard de analytics
- [ ] Implementar WebSockets para actualizaciones en tiempo real
- [ ] Agregar exportación de reportes (PDF/Excel)

---

## 👨‍💻 Autor


- GitHub: [@Kallheset](https://github.com/Kallheset)
- LinkedIn: [www.linkedin.com/in/argenis-manzanares-108b4a349]
- Email: <argenis010@gmail.com>

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- Django y Django REST Framework por el excelente framework
- Render.com por el hosting gratuito
- Cloudinary por el almacenamiento de media
- La comunidad de Python/Django por los recursos y documentación

---

<div align="center">

**⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Kallheset/Biblioteca-django-drf?style=social)](https://github.com/Kallheset/Biblioteca-django-drf/stargazers)

</div>
