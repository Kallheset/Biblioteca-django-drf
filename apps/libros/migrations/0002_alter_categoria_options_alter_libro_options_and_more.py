# Generated by Django 5.2.1 on 2025-05-27 22:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre'], 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='libro',
            name='calificacion',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='libros/'),
        ),
        migrations.AddField(
            model_name='libro',
            name='paginas',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
