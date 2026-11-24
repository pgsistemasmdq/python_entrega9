from django.shortcuts import render
from .models import Post


def inicio(request):
    """Página principal con las últimas publicaciones reales."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    return render(request, "posts/inicio.html", {"ultimos_posts": ultimos_posts})


def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    """Consulta las publicaciones visibles mediante el ORM."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})
