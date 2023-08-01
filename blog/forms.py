# forms = biblioteca que permite crear formularios
from django import forms
# post = clase creada en el archivo models.py
from .models import Post
# User = modelo que por defecto trae django permite agregar un username, password, email, etc . . . investiga mas sobre el Modelo User en la documentacion django
from django.contrib.auth.models import User

# Clase para crear un formulario con base a el modelo o table post y que contenga las mismas caracteristicas para editar y crear nuevas publicaciones
class Post_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Obtenemos el usuario actual del kwargs
        user = kwargs.pop('user', None)  
        super(Post_Form, self).__init__(*args, **kwargs)
        # Si hay un usuario actual, filtramos las opciones del campo "autor"
        if user:
            self.fields['autor'].queryset = User.objects.filter(id=user.id)

    # Con meta podemos obtener la tabla post del archivo models.py y usarlo como base para poder crear un formulario que edite y cree nuevas publicaciones
    class Meta:
        model = Post
        # Campos que obtenemos del modelo Post para agregarlos al formulario y asi editar o crear nuevas publicaciones
        fields = ['titulo', 'contenido', 'imagen', 'autor', 'categorias']
        # widgets = modificamos y agregamos estilos a los inputs del formulario
        # (attrs={'class': 'form-control form-input', 'placeholder': 'Escribe un título'}) = con el parametros attrs agregamos clases echas en css
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Escribe un título'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control form-input', 'placeholder': 'Escribe una descripción'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'autor': forms.Select(attrs={'class': 'form-control form-input'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control form-input'}),
        }
        # Mostramos mensajes de error si es que el formulario no es llenado de forma correctamente
        error_messages = {
            'titulo': {'required': 'Este campo es requerido.'},
            'contenido': {'required': 'Este campo es requerido.'},
            'autor': {'required': 'Este campo es requerido.'},
            'categorias': {'required': 'Este campo es requerido.'},
        }