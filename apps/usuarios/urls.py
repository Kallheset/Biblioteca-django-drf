from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', login_required(views.perfil_usuario), name='perfil'),
]
