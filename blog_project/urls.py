"""Rutas del sitio Django: admin y URLs de la aplicación posts."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("posts.urls")),
]
