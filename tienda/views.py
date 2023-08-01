from django.shortcuts import render
from tienda.models import Producto, Categoria_producto
# Create your views here.

# Con este modelo obtendremos todos los objetos o productos y mostrarlo en el template
def tienda(request):
    # en esta variable se guardan los productos en forma de lista
    productos=Producto.objects.all()
    # pasar como paramentro al renderizado de la plantilla la variable "producto"
    return render(request, "tienda/tienda.html",{"productos":productos})

def Categorias(request,categoria_id):
    # 
    categoria=Categoria_producto.objects.get(id=categoria_id)
    productos=Producto.objects.filter(categorias=categoria)
    # debe mostrar la categoria filtrada y los posts correspondientes de cada categoria filtrada
    return render(request,"tienda/categoria.html",{'categoria':Categoria_producto,"productos":productos})