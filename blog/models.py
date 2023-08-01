from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # max_length = permite indicar que el campo imagen en este caso solo puede recibir como maximo 1024 bytes por archivo
    imagen = models.ImageField(upload_to='blog', max_length=1024)
    # models.ForeignKey = utilizamos el modelo User que django trae por defecto para crear una llave foranea para la tabla Post
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.ManyToManyField = creamos una relacion muchos a muchos para relacionar la tabla post con la tabla categoria
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo