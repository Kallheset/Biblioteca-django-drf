from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import PerfilUsuarioForm, UserEmailForm
from .models import PerfilUsuario

def login_view(request):
    """
    Vista para el inicio de sesión de usuarios.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {username}!')
            next_url = request.GET.get('next', 'inicio')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'registration/login.html')

@require_http_methods(["GET", "POST"])
@login_required
def logout_view(request):
    """
    Vista para cerrar la sesión del usuario.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('usuarios:login')

def registro(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        # Validaciones
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('usuarios:registro')
            
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('usuarios:registro')
            
        if not username or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('usuarios:registro')
            
        from django.contrib.auth.models import User
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('usuarios:registro')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return redirect('usuarios:registro')
            
        try:
            # Crear el usuario
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            messages.success(request, f'¡Bienvenido {username}! Tu cuenta ha sido creada exitosamente.')
            return redirect('inicio')
            
        except Exception as e:
            messages.error(request, f'Error al registrar el usuario: {str(e)}')
            return redirect('usuarios:registro')
    
    # Si es una petición GET, mostrar el formulario de registro
    return render(request, 'registration/registro.html')

@login_required
def editar_perfil(request):
    user = request.user
    perfil, created = PerfilUsuario.objects.get_or_create(user=user)
    if request.method == 'POST':
        print('FILES:', request.FILES)  # DEBUG
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        email_form = UserEmailForm(request.POST, instance=user)
        if perfil_form.is_valid() and email_form.is_valid():
            perfil_form.save()
            email_form.save()
            print('AVATAR:', perfil_form.cleaned_data.get('avatar'))  # DEBUG
            from django.contrib import messages
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('usuarios:perfil')
    else:
        perfil_form = PerfilUsuarioForm(instance=perfil)
        email_form = UserEmailForm(instance=user)
    return render(request, 'usuarios/editar_perfil.html', {
        'perfil_form': perfil_form,
        'email_form': email_form,
    })

def perfil_usuario(request):
    """
    Vista para mostrar el perfil del usuario y sus préstamos activos.
    """
    from apps.prestamos.models import Prestamo
    from django.utils import timezone
    
    # Obtener préstamos activos del usuario
    prestamos_activos = Prestamo.objects.filter(
        usuario=request.user,
        fecha_devolucion__isnull=True
    ).select_related('libro')
    
    # Obtener historial de préstamos recientes (últimos 5)
    historial_prestamos = Prestamo.objects.filter(
        usuario=request.user,
        fecha_devolucion__isnull=False
    ).select_related('libro').order_by('-fecha_prestamo')[:5]
    
    context = {
        'usuario': request.user,
        'prestamos_activos': prestamos_activos,
        'historial_prestamos': historial_prestamos,
        'hoy': timezone.now().date()
    }
    
    return render(request, 'usuarios/perfil.html', context)
