from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage
# Create your views here.

# esta modo de enviar la informacion de lformulario al servidor de correo electronico funciona con el uso del constructor "EmailMessage"
def contacto(request):
    if request.method<="POST":
        formulario_contacto=Formulario_contacto(data=request.POST)
        # en esta instruccion le indicaremos a django que si el formulario ha sido llenado de forma correcta entonces que guarde en las variables nombre,email y contenido lo que se ingreso en los campos del formulario
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            # con EmailMessage hacemos que la informacion ingresada al formulario contacto sea enviada por correo al admin del sitio web
            email=EmailMessage("Mensaje desde app django",
            "El usuario: {} \n\n con el correo: {} \n\n escribe lo siguiente: {}".format(nombre,email,contenido),
            "",["jansalazmendoza@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
        return render(request, "contacto/contacto.html",{"mi_formulario":formulario_contacto})