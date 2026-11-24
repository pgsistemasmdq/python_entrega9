# Preentrega 9 - Modelos, SQLite y Admin de Django

Copia independiente de la evolución del módulo 8: conserva rutas, templates y CSS, y agrega **modelo Post, migración, panel admin y ORM**.


## Probar el panel admin

1. Abrí <http://127.0.0.1:8000/admin/> e ingresá con el superusuario que creaste.
2. Entrá a **Posts**, elegí **Agregar** y cargá al menos tres publicaciones (título, contenido, autor, estado).
3. Dejá al menos una en estado **Publicado**; otras pueden estar en **Borrador** o **Archivado**.
4. Abrí <http://127.0.0.1:8000/posts/> para verificar que aparecen **solo los publicados**.
5. Abrí la página inicial para ver los últimos tres posts publicados.

## Archivos clave

- `posts/models.py`: modelo `Post` y `__str__()`.
- `posts/migrations/0001_initial.py`: migración del modelo.
- `posts/admin.py`: `PostAdmin` con columnas y filtros.
- `posts/views.py`: consultas ORM a `Post.objects.filter(estado="publicado")`.
- `posts/templates/posts/lista_posts.html`: bucle `{% for post in posts %}`.

La BD `db.sqlite3` está excluida de Git. Cada copia de entrega crea su propia base al migrar.

