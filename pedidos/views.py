from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from pedidos.models import LineaPedido, Pedido, Financiacion

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Producto

from carro import context_processor
from pedidos import cuotas
from pedidos.cuotas import Cuotas

from .models import Tarjeta
from tienda.models import Producto
# Create your views here.


@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    monto_de_cuota = Cuotas(request)
    fdp = monto_de_cuota.cuotas['forma_de_pagar']
    cantidad_cuotas=monto_de_cuota.cuotas['cantidad']
    capital = context_processor.importe_total_carro(request)["importe_total_carro"]
    financiado= monto_de_cuota.cuota(capital,cantidad_cuotas)
    importe=monto_de_cuota.cuotas['monto_de_cuota']
    TEA=financiado

    financiacion=Financiacion.objects.create(cuotas=cantidad_cuotas,importe_cuota=importe,forma_de_pago=fdp)
    pedido=Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # cogemos el carro
    lineas_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    productos=list()
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido,
            financiacion=financiacion
            ))
        productos.append({'nombre':value['nombre'],'cantidad':value['cantidad'],'producto_id':key})
    LineaPedido.objects.bulk_create(lineas_pedido) # crea registros en BBDD en paquete

    cliente=request.user
    pedido=pedido
    lineas_pedido_lista=lineas_pedido
    #enviamos mail al cliente
    '''enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )'''
    #mensaje para el futuro
    #messages.success(request, "El pedido se ha creado correctamente")
    
    return render(request, "afterselling/pventa.html", {"forma_de_pagar": fdp,'cantidad_de_cuotas':cantidad_cuotas,'monto_de_cuota':importe,'cliente':cliente,'productos':lineas_pedido_lista,'names':productos})
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="cursos@pildorasinformaticas.es"
    #to=kwargs.get("email_usuario")
    to="aquí la dirección del destinatario"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)

def comenzar_compra(request):
    monto_de_cuota =Cuotas(request)
    monto_de_cuota.guardar_cuotas()
    tarjetas = Tarjeta.objects.all()

    return render(request, "pedidos/financiacion.html", {"tarjetas": tarjetas})

def agregar_cuota(request):

    monto_de_cuota=Cuotas(request)

    monto_de_cuota.aumentar()

    return redirect("comenzar_compra")

def disminuir_cuota(request):

    monto_de_cuota=Cuotas(request)

    monto_de_cuota.disminuir()

    return redirect("comenzar_compra")


def tarjetas(request):
    tarjetas = Tarjeta.objects.all()

    return render(request, "pedidos/financiacion.html", {"tarjetas":tarjetas })


def elegir (request, tarjeta_id):
    monto_de_cuota = Cuotas(request)
    tarjeta=Tarjeta.objects.get(id=tarjeta_id)
    monto_de_cuota.cuotas['forma_de_pagar']=tarjeta.nombre
    monto_de_cuota.cuotas['Descuento'] = tarjeta.descuento
    monto_de_cuota.cuotas['cantidad']=1
    monto_de_cuota.guardar_cuotas()
    monto_de_cuota.cuota(monto_de_cuota.capital,1)

    monto_de_cuota.guardar_cuotas()

    return redirect("comenzar_compra")

