"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from apps.libros import views as libros_views
from apps.prestamos import views as prestamos_views
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth.decorators import login_required

router = DefaultRouter()
router.register(r'libros', libros_views.LibroViewSet)
router.register(r'categorias', libros_views.CategoriaViewSet)
router.register(r'prestamos', prestamos_views.PrestamoViewSet, basename='prestamo')

# Cambiar el título del admin
admin.site.site_header = 'Panel de Administración - Biblioteca'
admin.site.site_title = 'Biblioteca Admin'
admin.site.index_title = 'Gestión de Biblioteca'

urlpatterns = [
    # URL del admin con un nombre menos predecible
    path('gestor-biblioteca/', include('django.contrib.admin.site.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # URLs de autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    # URLs de la aplicación
    path('', views.home, name='home'),
    path('libros/', libros_views.lista_libros, name='lista_libros'),
    path('prestamos/', prestamos_views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/crear/', prestamos_views.crear_prestamo, name='crear_prestamo'),
    path('prestamos/devolver/<int:prestamo_id>/', prestamos_views.devolver_libro, name='devolver_libro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
