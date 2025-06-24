from django.contrib import admin
from .models import Categoria, Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'disponible', 'stock')
    list_filter = ('disponible', 'categoria', 'autor')
    search_fields = ('titulo', 'isbn', 'autor__nombre')

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Libro, LibroAdmin)
