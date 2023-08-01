# para utilizar una variable global en un proyecto de django debemos implementar un procesador de contexto 
    # se trata de crear una variable que pueda ser usada mas haya de donde fue creada
        # crear una variable que vaya sumando el precio de productos en el carro

# la variable global se crea con una funcion con parametro de request, la variable "total" es la variable global

def importe_total_carro(request):
    total=0
    # para que los articulos se vayan sumando al carro debes verificar que el usuario este autenticado en un inicio de sesion
    if request.user.is_authenticated:
        if 'carro' in request.session:
            # recorre todos  los elementos que hay en el carro y sumar los importes
            for key, value in request.session["carro"].items():
                # operacion que incrementa el precio que hay en el carro dependiendo de los productos seleccionados
                total=total+float(value["precio"])
        else:
            total = "carro vacio"
    # en caso de que un usuario no este logeado e ingrese a la tienda muestre un mensaje de que debe hacer login
    else:
        total="Debes hacer login"
    return {"importe_total_carro":total}

