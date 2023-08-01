from django.urls import path
from proyectowebapp import views
# para poder utiliar los urls de la carpeta media se imporate el archivo "settings.py"
from django.conf import settings
# para poder utilizar los archivos static utilizamos la siguiente importacion
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="home"),
    path('politica/',views.politica, name="politica"),
    path('aviso/',views.aviso_legal, name="aviso"),
    path('cookies/',views.politica_cookies, name="cookies"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)