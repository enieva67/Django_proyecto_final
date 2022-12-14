from tabnanny import verbose
from django.db import models

from django.contrib.auth import get_user_model #devuelve el usuario activo actual
from django.db.models import F,Sum, FloatField  # para calcular el total de una orden de pedido
from tienda.models import Producto

User=get_user_model()

# Create your models here.

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) # Cuando se elimine un usuario sus pedidos se eliminirán en cascada
    created_at=models.DateTimeField(auto_now_add=True)   #Para le fecha de pedido automática

    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return str(self.id)


    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']

class Financiacion(models.Model):
    cuotas=models.IntegerField(default=1)
    importe_cuota=models.FloatField()
    forma_de_pago=models.CharField(max_length=30,default='contado efectivo')

    def __str__(self):
        return f'En {self.cuotas} cuotas de ${self.importe_cuota} \n Forma de pago {self.forma_de_pago}'

    class Meta:
        db_table='financiacion'
        verbose_name='Financiacion'
        verbose_name_plural='Financiacion'
        ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    financiacion=models.ForeignKey(Financiacion, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} \n {self.financiacion.forma_de_pago}'

    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']


class Tarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    descuento = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def get_descuento_porcentaje(self):
        return self.descuento * 100

    class Meta:
        verbose_name="Tarjeta"
        verbose_name_plural="Tarjetas"

