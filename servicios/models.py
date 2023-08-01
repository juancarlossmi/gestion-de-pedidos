from django.db import models

# Create your models here.

# la clase servicio es un objeto que contiene los campos titulo,contenido,imagen,created,updated

class servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    # ImageField: Campo de imagen
    imagen=models.ImageField(upload_to='servicio')
    # created: representa fecha de creacion del servicio y se puede ordenar por fecha al igual que "updated"
    # auto_now_add: agrega automaticamente la fecha de modificacion
    created=models.DateTimeField(auto_now_add=True)
    # updated: representa fecha de modificacion del servicio
    updated=models.DateTimeField(auto_now_add=True)

# django model Meta option: opciones adicionales que pueden introducirse aun modelo y para que sirven, https://docs.djangoproject.com/en/4.1/ref/models/options/
# para poder aplicar las opciones meta debemos crear una clase interna llamada "Meta"
    class Meta:
        # verbose_name: indica el nombre del servicio dentro de la base de datos
        verbose_name='servicio'
        # verbose_name_plural: indica el nombre del servicio dentro de la base de datos en plural
        verbose_name_plural='servicios'

# dentro de la clase servicio debemos crear una funcion str que devuelva el titulo del servicio
    def __str__(self):
        return self.titulo