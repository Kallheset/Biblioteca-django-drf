from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Prestamo, MAX_LIBROS_POR_USUARIO
from django.contrib.auth.models import User
from apps.libros.serializers import LibroSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
           

class PrestamoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    libro = LibroSerializer(read_only=True)
    libro_id = serializers.IntegerField(write_only=True, required=True)
    dias_prestamo = serializers.IntegerField(write_only=True, required=False, default=7)

    class Meta:
        model = Prestamo
        fields = ['id', 'usuario', 'libro', 'libro_id', 'fecha_prestamo', 'fecha_devolucion_esperada', 'fecha_devolucion', 'dias_prestamo']
        read_only_fields = ['usuario', 'fecha_prestamo', 'fecha_devolucion_esperada', 'fecha_devolucion']

    def create(self, validated_data):
        # Eliminar dias_prestamo si está presente, ya que no es campo del modelo
        validated_data.pop('dias_prestamo', None)
        try:
            prestamo = Prestamo.objects.create(**validated_data)
            return prestamo
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict if hasattr(e, 'message_dict') else e.messages)

    def update(self, instance, validated_data):
        # Solo permitir actualizar la fecha de devolución
        if 'fecha_devolucion' in validated_data:
            instance.devolver()
        return instance
