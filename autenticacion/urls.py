from django.urls import path
# del archivo vistas import la clase "VRegistro"
from .views import VRegistro, cerrar_sesion, logear


urlpatterns = [
    # as_view= convierte las clases en vistas
    path('', VRegistro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
]
