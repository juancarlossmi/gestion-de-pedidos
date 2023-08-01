from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Categoria, Post

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Si es un superusuario, se mostrarán todos los usuarios disponibles en el campo de clave foránea. Si no es un superusuario, se mostrará solo el usuario actual, restringiendo la selección del autor del post solo al usuario que está iniciando sesión.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "autor":
            # Permitimos que un administrador pueda asignar cualquier usuario como autor de un post
            if request.user.is_superuser:
                kwargs["queryset"] = User.objects.all()
            else:
                # , mientras que un usuario normal solo podrá asignarse a sí mismo como autor de un post.
                kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
