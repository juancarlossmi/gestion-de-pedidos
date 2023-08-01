from django.contrib import admin
# .: indica que nos moveremos dentro del mismo directorio, como el archivo "admin.py" y models se encuentran en el mismo directorio hacemos uso del punto paraa indicar que nos moveremos en el mismo directorio
from .models import servicio

# Register your models here.


# para poder mostrar los campos created y updated debemos crear una clase que muestre los campos solo para lectura
# readonly_fields: campos solo para lectura
class servicioadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# con esta ilnea se registra la aplicacion en 127.0.0.1:8000/admin
admin.site.register(servicio,servicioadmin)