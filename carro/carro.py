# la clase "CARRO" realizara las siguiente tareas
    # 1. MANEJO DE SESION
    # 2. AGREGAR PRODUCTOS
    # 3. ELIMINAR PRODUCTOS
    # 4. RESTAR PRODUCTOS
    # 5. VACIAR EL CARRO

# 1. MANEJO DE SESION
class Carro:
    # los constructores son responsables de las tareas
    def __init__(self, request):
    # requets= alamacenamos la peticion para acceder al carro
        self.request=request
    # con esta linea construimos el inicio de sesion
        self.session=request.session
    # construir un carro de compra para la sesion actual 
        carro=self.session.get("carro")
    # cuando el usuario agrega un articulo por primera vez debemos igualar la sesion del usuario con el carro actual, si el usario se va al volver debemos comprobar si esa sesion tiene carro en caso de que no hubiera carro debemos crearlo y en caso contrario debemos utilizar el carro que esta guardado en la variable carro
        
        # debemos utilizar un diccionario para almacenar las caracteristicas de un producto
        if not carro:
            carro=self.session["carro"]={}
        # else:
        # con esta linea siempre se crea el carro sin tener en cuenta si hay sesion iniciada o no, siempre se crea el carro
        self.carro=carro

# 2. AGREGAR PRODUCTOS
    def agregar(self, producto):
        # realizar una comprobacion: si un producto no esta en las claves del carro agregalos (traducido a codigo seria . . . )
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        # y si la clave de el producto ya esta en el carro entonces debes agregar una unidad mas de ese producto seleccionado (traducido a codigo seria . . . )
        else:
            # para cada clave:Valor que tengamos en nuestro carro comprobar si la clave del producto corresponde con el ID de alguno de los productos que ya estaba en el carro
            for key, value in self.carro.items():
                # comprobar si la clave del producto corresponde al id de alguno de los productos que ya tenemos en el carro
                if key==str(producto.id):
                    # si el if anterior es valido entonces en la propiedad "CANTIDAD" del producto sera value["cantidad"]+1
                    # INCREMENTAR EL NUMERO DE UNIDADES DE UN PRODUCTO
                    value["cantidad"]=value["cantidad"]+1
                    # esta linea suma los precios segun la unidad elegida
                    value["precio"]=float(value["precio"])+producto.precio
                    # si el articulo ya fue encontrado que haga "BREAK" y no recorra mas la lista
                    break
        # actualizar el carro para poder guardarlo en la sesion: esta funcion se encargara de sumar o restar productos ()
        self.guardar_carro()
    # funcion que nos permite guardar la sesion
    def guardar_carro(self):
        # linea que se encarga de ir guardando la sesion si se suman articulos o si se restan o eliminan productos
        self.session["carro"]=self.carro
        # para que la linea anterior tenga efecto agregar lo siguiente  . . .
        self.session.modified=True
        
# 3. ELIMINAR PRODUCTOS
    # crear una distincion entre eliminar y borrar

    # funcion que elimina todos los productos recibe como parametros (self, producto=al producto que queresmos eliminar)
    def eliminar(self,producto):
        # 1. almacenar id del producto
        producto.id=str(producto.id)
        # 2. comprobar si el producto existe
        if producto.id in self.carro:
            # 3. si el producto ya existe entonces quita el producto con ayuda de la funcion del
            del self.carro[producto.id]
            # 4. una vez eliminado el producto guardar el carro nuevamente
            self.guardar_carro()
    
    # funcion que resta productos por unidades recibe como parametros (self, producto=al producto que queresmos eliminar)
    def restar(self, producto):
        # 1. para cada clave valor de los elementos del carro comprobar que exite la clave del id del producto que queremos restar
        for key, value in self.carro.items(): 
            # 2. comprobar si el producto existe
            if key==str(producto.id):
                # esta linea resta los precios segun la unidad elegida
                value["precio"]=float(value["precio"])-producto.precio
                # 3. si el producto ya existe entonces resta una unidad del producto
                value["cantidad"]=value["cantidad"]-1
                # controlar que ocurre si restamos unidades de un producto que solo tiene una unidad es decir el articulo debe desaparecer ya que hay 0 unidades
                # en el caso de que el articulo al que queremos restarle una unidad y ese articulo solo tiene una unidad entonces elimina el productos es decir 1-1=0 o elimnar producto
                if value["cantidad"]<1:
                    # si el if anterior se cumple entonces elimina el producto al cual le restamos la unidad
                    self.eliminar(producto)
                # si encuentra el producto del que quiera restar la cantidad que se salga del bucle
                break
        # 4. una vez restado el producto guardar el carro nuevamente
        self.guardar_carro()
     
# 5. VACIAR EL CARRO
    # funcion que elimina todos los objetos del carro a peticion del usuario es decir vacear todo el carro
    def limpiar_carro(self):
        # cuando se limpia el carro construir un diccionario vacio
        self.session["carro"]={}
        # recuerda que cada vez que modificamos la session debemos ejecutar la siguiente linea
        self.session.modified=True