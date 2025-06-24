from rest_framework import viewsets
from .models import Autor
from .serializers import AutorSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})