from django.urls import path
from proyectowebapp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('politica/',views.politica, name="politica"),
    path('aviso/',views.aviso_legal, name="aviso"),
    path('cookies/',views.politica_cookies, name="cookies"),
]
