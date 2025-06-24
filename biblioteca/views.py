from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, '¡Bienvenido!')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión')
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registration/registro.html')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, '¡Registro exitoso!')
            return redirect('lista_libros')
        except IntegrityError:
            messages.error(request, 'El nombre de usuario ya existe')
    
    return render(request, 'registration/registro.html')