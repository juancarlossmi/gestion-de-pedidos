"""
URL configuration for proyectoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# para poder utiliar los urls de la carpeta media se imporate el archivo "settings.py"
from django.conf import settings
# para poder utilizar los archivos static utilizamos la siguiente importacion
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('proyectowebapp.urls')),
    path("servicios/", include('servicios.urls')),
    path("blog/", include('blog.urls')),
    path("contacto/", include('contacto.urls')),
    path("tienda/", include('tienda.urls')),
    path("carro/", include('carro.urls')),
    path("autenticacion/", include('autenticacion.urls')),
    path("pedidos/", include('pedidos.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)