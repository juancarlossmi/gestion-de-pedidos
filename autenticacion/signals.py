# el archivo signals sirve para definir y manejar señales, las señales son eventos que se generan en ciertos momentos dentro del ciclo de la app
# cuando se crea, elimina o edita un objeto en la bases de datos de django se ejecutan las señales que 
# PERMITEN REALIZAR ACCIONES ADICIONALES antes o despues de que ocurra el evento (elimnar, editar objetos)
# en este caso utilizamos sigunals cuando un usuario nuevo es registrado con la funcion assign_user_to_group agregamos automaticamente a los usuarios nuevos a un grupo definido anteriormente por el admin del sitio web
# que permite a los usuarios nuevos crear editar actualizar y eliminar publicaciones realizadas por ellos

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# obtenemos el modelo del usuario que se ha registrado
User = get_user_model()

# receiver = se utiliza para conectar señales con funciones de receptor como assign_user_to_group
@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        # Obtenemos el objeto del grupo llamado "usuarios nuevos" desde la base de datos
        group = Group.objects.get(name='usuarios nuevos')
        # Agregamos al nuevo usuario registrado al grupo "usuarios nuevos"
        instance.groups.add(group)
        # Marcar al usuario como miembro staff
        instance.is_staff = True
        # Activar al usuario
        instance.is_active = True
        # Guardamos los cambios realizados al objeto de usuario en la base de datos
        instance.save()

