from django.contrib import admin
from .models import Pedido, Linea_Pedido

# Register your models here.

admin.site.register([Pedido, Linea_Pedido])