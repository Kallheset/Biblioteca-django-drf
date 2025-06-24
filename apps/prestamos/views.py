from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.contrib import messages
from .models import Prestamo
from .serializers import PrestamoSerializer
from apps.libros.models import Libro
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def lista_prestamos(request):
    prestamos_activos = Prestamo.objects.filter(usuario=request.user, fecha_devolucion__isnull=True)
    prestamos_devueltos = Prestamo.objects.filter(usuario=request.user, fecha_devolucion__isnull=False)
    return render(request, 'prestamos.html', {
        'prestamos_activos': prestamos_activos,
        'prestamos_devueltos': prestamos_devueltos
    })

@login_required
def crear_prestamo(request):
    if request.method == 'POST':
        try:
            libro = Libro.objects.get(id=request.POST['libro'])
            Prestamo.objects.create(
                usuario=request.user,
                libro=libro,
                fecha_devolucion_esperada=timezone.now().date() + timezone.timedelta(days=7)
            )
            messages.success(request, 'Préstamo creado exitosamente.')
        except Exception as e:
            messages.error(request, str(e))
    return redirect('lista_prestamos')

@login_required
def devolver_libro(request, prestamo_id):
    try:
        prestamo = Prestamo.objects.get(id=prestamo_id, usuario=request.user)
        prestamo.devolver()
        messages.success(request, 'Libro devuelto exitosamente.')
    except Exception as e:
        messages.error(request, str(e))
    return redirect('lista_prestamos')

class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prestamo.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        libro = Libro.objects.get(id=self.request.data.get('libro_id'))
        dias_prestamo = int(self.request.data.get('dias_prestamo', 7))
        serializer.save(
            usuario=self.request.user,
            libro=libro,
            fecha_devolucion_esperada=timezone.now().date() + timezone.timedelta(days=dias_prestamo)
        )
        return redirect('lista_prestamos')

    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        prestamo = self.get_object()
        try:
            prestamo.devolver()
            return redirect('lista_prestamos')
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Lista los préstamos activos del usuario"""
        prestamos_activos = self.get_queryset().filter(fecha_devolucion__isnull=True)
        serializer = self.get_serializer(prestamos_activos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def historial(self, request):
        """Lista el historial de préstamos del usuario"""
        prestamos = self.get_queryset().filter(fecha_devolucion__isnull=False)
        serializer = self.get_serializer(prestamos, many=True)
        return Response(serializer.data)
