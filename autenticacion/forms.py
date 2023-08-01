from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationWithEmailForm(UserCreationForm):
    # Creamos el formulario de autenticacion con un placeholder para ayudar al usuario
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'placeholder': 'Ingresa un nombre de usuario.'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu dirección de correo electrónico.'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa una contraseña segura.'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']