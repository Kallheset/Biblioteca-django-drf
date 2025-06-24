from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'biografia', 'nacionalidad']
        extra_kwargs = {
            'nombre': {'required': True, 'min_length': 2},
            'nacionalidad': {'required': True},
            'biografia': {'required': False, 'allow_blank': True}
        }

    def validate_nombre(self, value):
        # Permitir actualizar el mismo autor sin error de unicidad
        qs = Autor.objects.filter(nombre__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Ya existe un autor con este nombre")
        return value