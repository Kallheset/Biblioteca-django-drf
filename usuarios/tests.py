from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UsuariosViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'usuario_test'
        self.password = 'password1234'
        self.email = 'test@example.com'
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)

    def test_registro_exitoso(self):
        response = self.client.post(reverse('usuarios:registro'), {
            'username': 'nuevo_usuario',
            'email': 'nuevo@example.com',
            'password': 'nueva_clave123',
            'password2': 'nueva_clave123',
        })
        self.assertEqual(response.status_code, 302)  # Redirige tras registro
        self.assertTrue(User.objects.filter(username='nuevo_usuario').exists())

    def test_registro_passwords_no_coinciden(self):
        response = self.client.post(reverse('usuarios:registro'), {
            'username': 'fail_usuario',
            'email': 'fail@example.com',
            'password': 'clave1',
            'password2': 'clave2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='fail_usuario').exists())

    def test_registro_password_corta(self):
        response = self.client.post(reverse('usuarios:registro'), {
            'username': 'fail_usuario2',
            'email': 'fail2@example.com',
            'password': 'short',
            'password2': 'short',
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='fail_usuario2').exists())

    def test_login_exitoso(self):
        response = self.client.post(reverse('usuarios:login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)  # Redirige tras login

    def test_login_fallido(self):
        response = self.client.post(reverse('usuarios:login'), {
            'username': self.username,
            'password': 'clave_incorrecta',
        })
        self.assertEqual(response.status_code, 200)  # Vuelve a mostrar login
        self.assertContains(response, 'Usuario o contraseña incorrectos')

    def test_perfil_requiere_autenticacion(self):
        response = self.client.get(reverse('usuarios:perfil'))
        self.assertEqual(response.status_code, 302)  # Redirige a login

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('usuarios:logout'))
        self.assertEqual(response.status_code, 302)  # Redirige tras logout
