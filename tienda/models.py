from django.db import models
# como utilizaremos la clase "USERS" para relacionar cada usuario con un autor entonces importamos la clase "users"
from django.contrib.auth.models import User

# Create your models here.

class Categoria_producto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_producto'
        verbose_name_plural='categorias_productos'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    # Campo con clave foranea: es decir es el campo con el que relacionaremos la tabla o clase "Producto" con la tabla o clase de "Categoria_producto"
    categorias=models.ForeignKey(Categoria_producto,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda',null=True, blank=True)
    precio=models.FloatField()
    # con "default=True" indicamos que por defecto si no se indica nada la disponibilidad es TRUE
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return self.nombre