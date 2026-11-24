from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelsYVistaTests(TestCase):
    def test_post_se_representa_por_titulo(self):
        post = Post.objects.create(titulo="Aprendiendo Django", contenido="Texto", autor="Carlos", estado="publicado")
        self.assertEqual(str(post), "Aprendiendo Django")

    def test_listado_solo_muestra_publicados(self):
        Post.objects.create(titulo="Visible", contenido="Sí", autor="Carlos", estado="publicado")
        Post.objects.create(titulo="No visible", contenido="No", autor="Carlos", estado="borrador")
        respuesta = self.client.get(reverse("posts:lista_posts"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Visible")
        self.assertNotContains(respuesta, "No visible")
        self.assertTemplateUsed(respuesta, "posts/lista_posts.html")
