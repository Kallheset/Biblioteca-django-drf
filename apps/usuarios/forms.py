from django import forms
from .models import PerfilUsuario
from django.contrib.auth.models import User

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['direccion', 'fecha_nacimiento', 'telefono', 'apodo', 'avatar']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
