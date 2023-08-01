from django.shortcuts import render
# para poder acceder a los metodos y funciones de la clase "Carro" debemos importarlo
from .carro import Carro
# para poder acceder a las catacteristicas de los productos importar el modelo "Producto"
from tienda.models import Producto
# con "redirect" logrearemos que cada vez que se agregue un producto o elimine debemos redireccionar a la pagina de la tienda para que refleje los cambios realizados
from django.shortcuts import redirect

# Create your views here.

# vista para agregar productos nuevos al carro recibe como parametro la identificacion de los produtos ("producto_id")
def agregar_producto(request, producto_id):
    # con la variable carro y la clase creada anteriormente Carro se crea el carro de compras
    carro=Carro(request)
    # con esta linea obtenemos el producto que agregaremos al carro
    producto=Producto.objects.get(id=producto_id)
    # con esta linea agregamos el producto al carro
    carro.agregar(producto=producto)
    # utilizamos la funcion "redirect" ya que cada vez que carguemos una pagina debemos obtener la informacion que tenia el carro antes de volver a cargar la pagina
    return redirect("tienda")

# vista para eliminar productos recibe como parametro la identificacion de los produtos ("producto_id")
def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    # con esta linea eliminamos el producto al carro estas funciones estan en el archivo "carro.py"
    carro.eliminar(producto=producto)
    return redirect("tienda")

# vista para restar productos uno por uno recibe como parametro la identificacion de los produtos ("producto_id")
def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    # con esta linea restamos el producto al carro estas funciones estan en el archivo "carro.py"
    carro.restar(producto=producto)
    return redirect("tienda")

# vista para limpia el carro recibe como parametro la identificacion de los produtos ("producto_id")
def limpiar_producto(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")