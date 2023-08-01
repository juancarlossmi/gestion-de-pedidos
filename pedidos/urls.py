from django.urls import path
from .import views

urlpatterns = [
    path("", views.procesar_pedido, name="procesar_pedido"),
    path("gracias/", views.gracias, name="gracias")
]