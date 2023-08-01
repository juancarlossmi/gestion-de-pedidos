from django.urls import path
from . import views
from .views import create_post

urlpatterns = [
    path('',views.blog, name="blog"),
    path('categoria/<int:categoria_id>/',views.categoria, name="categoria"),
    path('eliminar_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('editar_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('create/', create_post, name="create"),
]