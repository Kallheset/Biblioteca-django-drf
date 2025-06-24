from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.autores.models import Autor

class AutoresAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.autor = Autor.objects.create(nombre='Gabriel García Márquez', nacionalidad='Colombia', biografia='Autor de Cien años de soledad')

    def test_listar_autores(self):
        url = reverse('autor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_crear_autor(self):
        url = reverse('autor-list')
        data = {
            "nombre": "Julio Cortázar",
            "nacionalidad": "Argentina",
            "biografia": "Autor de Rayuela"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Autor.objects.filter(nombre="Julio Cortázar").exists())

    def test_update_autor(self):
        url = reverse('autor-detail', args=[self.autor.id])
        data = {
            "nombre": "Gabriel García Márquez",
            "nacionalidad": "México",
            "biografia": "Vivió en México muchos años"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.nacionalidad, "México")

    def test_delete_autor(self):
        url = reverse('autor-detail', args=[self.autor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Autor.objects.filter(id=self.autor.id).exists())
