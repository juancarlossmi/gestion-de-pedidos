from django.db import models


# Create your models here.

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)
    telefono=models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name="Contacto"
        verbose_name_plural="Contactos"
    def __str__(self):
        return self.nombre