from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    direccion = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    apodo = models.CharField(max_length=50, blank=True)
    from cloudinary_storage.storage import MediaCloudinaryStorage
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        storage=MediaCloudinaryStorage()
    )

    def __str__(self):
        return self.user.username
