from django.shortcuts import render, redirect
# Permite crear vistas más simples y reutilzables para la aplicación, en lugar de crear vistas desde cero
from django.views.generic import View
# Crear formularios de registro para usuarios de forma automatica y guarda la informacion en la base de datos de nuestra pagina web# Create your views here; crea formularios de registro y formulario de login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# importacion que permite hacer "login" a un usuario
from django.contrib.auth import login, logout, authenticate
# esta importacion nos permite manejar los mensajes de error que cometa el usuario
from django.contrib import messages
from .forms import UserCreationWithEmailForm

# Create your views here.

class VRegistro(View):
    # funcion que renderiza el formulario
    def get(self, request):
        # variable que crea y guarda el formulario
        form=UserCreationWithEmailForm()
        return render(request,"registro/registro.html",{"form":form})

    # funcion que envia la informacion del formulario y la almacena en la base de datos
    def post(self,request):
        # variable que crea el formulario con la informacion que el usuario ha ingresado ("usuario/contraseña")
        form=UserCreationWithEmailForm(request.POST)
        if form.is_valid():
            # variable donde se guarda la informacion del formulario con la funcion "save" ya almacenamos la informacion en la base de datos
            usuario=form.save()
            # si una cuenta se registra como nueva debemos hacer que este "loggin" automatico
            login(request,usuario)
            return redirect("home")
        else:
            # debemos recorrer todos los mensajes de error que el usuario haya recorrido
            # por cada mensaje de error que haya en el formulario
            for msg in form.error_messages:
                # muestra los errores que se crearon por el usuraio muestra un "array" de errores posibles
                messages.error(request,form.error_messages[msg])
            # devolver el formulario con los errores ingresados
            return render(request,"registro/registro.html",{"form":form})

# cuando se llame a esta vista se cerrara la sesion
def cerrar_sesion(request):
    # logout= instruccion que cierra sesion del usuario
    logout(request)
    return redirect("home")

def logear(request):
    # si has pulsado el boton entonces
    if request.method=="POST":
        # form=contiene el formulario de autenticacion aue se crea de manera automarica
        form=AuthenticationForm(request, data=request.POST)
        # valida el formulario de autenticacion si no hay error en la informacion entonces
        if form.is_valid():
            # obten la informacion que el usuario ingreso al cuadro de texto
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            # con esta linea autenticamos aun usuario
            usuario=authenticate(username=nombre_usuario, password=contra)
            # si el usuario es correcto o existe entonces
            if usuario is not None:
                # instruccion que hace login con usuario y contraseña
                login(request,usuario)
                # depues de ingresar a la sesion el usuario es redirigido a "home"
                return redirect("home")
            # si el usuario no existe entonces
            else:
                # muestra este mensaje de error
                messages.error(request, "usuario no valido")
        # si la informacion del usuario no es introducida correctamente entonces
        else:
            # muestra este mensaje de error
            messages.error(request, "Ingresa un usuario y contraseña valida")
    # para crear un formulario de login usamos la clase "AuthenticationForm"
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})
