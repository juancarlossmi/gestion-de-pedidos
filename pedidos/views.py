from django.shortcuts import redirect, render
# importacion de "login_required"
from django.contrib.auth.decorators import login_required
# importacion del archivo "carro.py" para poder manipular sus propiedades
from carro.carro import Carro
# importacion del modelo "Pedido"
from pedidos.models import Linea_Pedido, Pedido
# importacion que nos muestra los mensajes emergenetes
from django.contrib import messages
# instruccion que renderiza el pedido del usuario en un html para el admin
from django.template.loader import render_to_string
# instruccion que convierte el html en un texto mas legible
from django.utils.html import strip_tags
# instruccion que procesa la informacion de strip tags para que el admin reciba el pedido del usuario
from django.core.mail import send_mail

# Create your views here.

# login_required= si un usuario esta logeado puede hacer pedidos en caso contrario no puede hacer pedidos
@login_required(login_url="/autenticacion/logear")
# vista que procesa los pedidos
def procesar_pedido(request):
    # cuando la funcion sea llamada se dara de alta un pedido con la variable "pedido" donde "create" especifica el usuario que ha generado el pedido y saber quien es
    pedido=Pedido.objects.create(user=request.user)
    # con la variable carro podemos manipular las propiedades del carro para poder ver los items del carro debemos recorrer uno a uno para poder alamcenarlos en la "Linea_Pedido" para saber el nombre del pedido cantidades del pedido y precio del pedido
    carro=Carro(request)
    # lineas_pedido= el carro contendra diferentes items y deben estar contenidos en una lista 
    lineas_pedido=list()
    # por cada clave:valor que hay en los items del carro entonces
    for key, value in carro.carro.items():
        # cada item que te encuentres agrega en la lista "lineas_pedido, el producto_id, catidad, user y pedido
        lineas_pedido.append(Linea_Pedido(
            # producto_id = id del producto
                # donde key = es la clave del producto
            producto_id=key,
            # cantidad = hace referencia a "value" del bucle "for" y debemos darle el valor a la cantidad de los productos que hay en el carro
            cantidad=value['cantidad'],
            # user = indica el nombre del usuario que dio de alta el pedido
            user=request.user,
            # pedido = hace referencia a la app "pedido"
            pedido=pedido
        ))
    # este metodo aplica varias instrucciones "INSERT_INTO"
    Linea_Pedido.objects.bulk_create(lineas_pedido)
    # Calcular el total
    total_a_pagar = sum(linea.producto.precio * linea.cantidad for linea in lineas_pedido)
    # antes de que el mensaje se muestre se enviara un mail al usuario para que vea el pedido que ha generado
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        # nombre de usuario del objeto user
        nombre_usuario=request.user.username,
        # correo de usuario del objeto correo
        email_usuario=request.user.email,
        # Agregar el total_a_pagar al contexto del correo
        total_a_pagar=total_a_pagar
    )
    # mensaje que muestra al usuario que el pedido se genero de forma correcta
    # messages.success(request,"El pedido se ha generado correctamente")

    
    # enviar al usuario a "tienda despues de confirmar que el pedido es correcto" y limpiar el carro
    carro.limpiar_carro()
    return render(request, "pedidos/gracias.html")

# **kwargs = para que una funcion reciva un numero indefinido de parametros
def enviar_mail(**kwargs):
    # variable que guarda el asunto del mail y el usuario lo vea
    asunto="Gracias por el pedido"
    # mensaje =  esta variable mostrara toda la informacion del pedido, recibe como contexto la informacion del pedido generado por medio de los kwargs
    mensaje=render_to_string("emails/pedido.html", {
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombre_usuario":kwargs.get("nombre_usuario"),
        "email_usuario":kwargs.get("email_usuario"),
        # Pasar el total_a_pagar al contexto
        "total_a_pagar": kwargs.get("total_a_pagar")
        })
    # debemos omitir los caracteres de etiqueta html que haya en "mensaje"
    mensaje_texto=strip_tags(mensaje)
    # de donde procede la informacion del pedido en especifico cual es el correo que enevia la informacion del pedido email del admin
    from_email="jcsmidev@gmail.com"
    # to=kwargs.get("email_usuario") =  email que ingresa el usuario cuando se registra esta opcion se utiliza siempre y cuando el usuario registrado tenga un correo valido al cual eniarle correos del admin confirmando el pedido
    to=kwargs.get("email_usuario")
    # send_mail = funcion que envia los email a los usuarios desde un admin a
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje,fail_silently=False)


def gracias(request):
    return render(request, "pedidos/gracias.html")