from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    nacionalidad = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombre

    def clean(self):
        # Longitud mínima
        if len(self.nombre) < 2:
            raise ValidationError({'nombre': 'El nombre debe tener al menos 2 caracteres.'})
        # Unicidad (case insensitive)
        if Autor.objects.exclude(pk=self.pk).filter(nombre__iexact=self.nombre).exists():
            raise ValidationError({'nombre': 'Ya existe un autor con este nombre.'})
        # Nacionalidad requerida
        if not self.nacionalidad:
            raise ValidationError({'nacionalidad': 'La nacionalidad es requerida.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)