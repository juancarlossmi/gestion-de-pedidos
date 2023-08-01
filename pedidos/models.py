from django.db import models
# esta funcion nos devuelve el nombre del usuario logeado
from django.contrib.auth import get_user_model
# importacion del modelo producto
from tienda.models import Producto
# esta importacion nos ayuda a calcular el total de la suma de los pedidos
from django.db.models import F, Sum, FloatField
from django.contrib.auth.models import User

# Create your models here.

# variable que guarda el nombre del usuario actual logeado
user=get_user_model()
# clase que construira la tabla "Pedido"
class Pedido(models.Model):
    # la tabal tendra un campo usuario y la clave es foranea ya que las tablas estan relacionas por "id_user"
        # si se elimina un usuario en una tabla se eliminaran los pedidos que se hayan realizado en la otra tabla de pedidos
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # en este campo se registra el momento exacto cuando se registra un pedido
    created_at=models.DateTimeField(auto_now_add=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)

    # el decorador "property" nos devuelve la suma del total de los productos agregados al carro
    @property
    def total(self):
        # una vez creado el modelo "Pedido" agregaremos la funcion de sumar las cantidades de los prductos y mostrar el resultado
            # con la funcion "set.aggregate" agrega el precio y la cantidad de los productos en la variable global "total"
        return self.linea_pedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"] or FloatField(0)
    
    def __str__(self):
        return f"Pedido {self.id} - Usuario: {self.user}"

        
    class Meta:
        # db_table = indica el nombre que tendra la tabla en la base de datos
        db_table="pedidos"
        verbose_name="pedido"
        verbose_name_plural="pedidos"
        # ordering = idica que la informacion esta ordenada por "id"
        ordering=['id']

# campos de la linea de pedidos
class Linea_Pedido(models.Model):
    # on_delete= si el usuario es eliminado entonces se elimina todo el contenido relacionado con ese usuario
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # ForeignLekey = clave forane
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    # cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    # esta funcion devuelve la cantidad de productos y el nombre del producto esto es a vista de "admin"
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    # nombre con los que identificaremos nuestra clase "Linea_Pedido"
    class Meta:
        db_table="linea_pedido"
        verbose_name="Linea pedido"
        verbose_name_plural="Lineas pedidos"
        ordering=['id']