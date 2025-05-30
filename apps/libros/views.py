from rest_framework import viewsets, filters
from .models import Categoria, Libro
from .serializers import CategoriaSerializer, LibroSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib import messages
from apps.prestamos.models import Prestamo
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['disponible', 'categoria', 'autor']
    search_fields = ['titulo', 'isbn', 'autor__nombre']
    ordering_fields = ['titulo', 'fecha_publicacion']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

@login_required
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})

@login_required
def crear_libro(request):
    if request.method == 'POST':
        try:
            libro = Libro.objects.create(
                titulo=request.POST['titulo'],
                autor_id=request.POST['autor'],
                categoria_id=request.POST['categoria'],
                isbn=request.POST['isbn'],
                descripcion=request.POST.get('descripcion', ''),
                fecha_publicacion=request.POST['fecha_publicacion'],
                stock=request.POST.get('stock', 1)
            )
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('lista_libros')
        except ValidationError as e:
            messages.error(request, str(e))
    return render(request, 'crear_libro.html')

@login_required
def prestar_libro(request, libro_id):
    try:
        libro = Libro.objects.get(id=libro_id)
        if libro.disponible:
            dias = int(request.POST.get('dias_prestamo', 7))
            Prestamo.objects.create(
                usuario=request.user,
                libro=libro,
                fecha_devolucion_esperada=timezone.now().date() + timezone.timedelta(days=dias)
            )
            messages.success(request, 'Libro prestado exitosamente.')
        else:
            messages.error(request, 'El libro no está disponible.')
    except (Libro.DoesNotExist, ValidationError, Exception) as e:
        messages.error(request, str(e))
    return redirect('lista_libros')

@login_required
def mis_prestamos(request):
    prestamos_activos = Prestamo.objects.filter(
        usuario=request.user,
        fecha_devolucion__isnull=True
    ).select_related('libro')
    
    prestamos_devueltos = Prestamo.objects.filter(
        usuario=request.user,
        fecha_devolucion__isnull=False
    ).select_related('libro').order_by('-fecha_devolucion')
    
    return render(request, 'prestamos.html', {
        'prestamos_activos': prestamos_activos,
        'prestamos_devueltos': prestamos_devueltos
    })

@login_required
def devolver_libro(request, prestamo_id):
    try:
        prestamo = Prestamo.objects.get(id=prestamo_id, usuario=request.user)
        if prestamo.fecha_devolucion:
            messages.warning(request, 'Este libro ya ha sido devuelto.')
        else:
            prestamo.fecha_devolucion = timezone.now().date()
            prestamo.save()
            
            # Marcar el libro como disponible
            libro = prestamo.libro
            libro.disponible = True
            libro.save()
            
            messages.success(request, 'Libro devuelto exitosamente.')
    except Prestamo.DoesNotExist:
        messages.error(request, 'Préstamo no encontrado.')
    
    return redirect('lista_prestamos')