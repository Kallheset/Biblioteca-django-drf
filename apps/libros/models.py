from django.db import models
from apps.autores.models import Autor
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = CloudinaryField(
        'imagen',
        folder='biblioteca/categorias',
        resource_type='image',
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    isbn = models.CharField(max_length=13, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)
    imagen = CloudinaryField(
        'imagen',
        folder='biblioteca/libros',
        resource_type='image',
        null=True,
        blank=True
    )
    descripcion = models.TextField(blank=True)
    paginas = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    calificacion = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
    )
    stock = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo

    def clean(self):
        # Título requerido
        if not self.titulo or len(self.titulo) < 2:
            raise ValidationError({'titulo': 'El título es requerido y debe tener al menos 2 caracteres.'})
        # ISBN requerido y longitud
        if not self.isbn or len(self.isbn) != 13 or not self.isbn.isdigit():
            raise ValidationError({'isbn': 'El ISBN debe tener 13 dígitos numéricos.'})
        # Unicidad de ISBN
        if Libro.objects.exclude(pk=self.pk).filter(isbn=self.isbn).exists():
            raise ValidationError({'isbn': 'Ya existe un libro con este ISBN.'})
        # Fecha de publicación requerida y no futura
        if not self.fecha_publicacion:
            raise ValidationError({'fecha_publicacion': 'La fecha de publicación es requerida.'})
        if self.fecha_publicacion > timezone.now().date():
            raise ValidationError({'fecha_publicacion': 'La fecha de publicación no puede ser futura.'})
        # Autor requerido
        if not self.autor:
            raise ValidationError({'autor': 'El autor es requerido.'})
        # Stock no puede ser negativo
        if self.stock < 0:
            raise ValidationError({'stock': 'El stock no puede ser negativo.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)