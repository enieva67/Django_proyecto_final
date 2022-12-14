from django.shortcuts import render
from .forms import EncuestaForm
from django.views import View

from tienda.models import Producto
from carro.carro import Carro
from .models import Encuesta
# Create your views here.

def pventa(request):
    return render(request, "afterselling/pventa.html")

def opinion(request,producto_id):
    opiniones=Encuesta.objects.filter(producto=producto_id)
    producto=Producto.objects.get(pk=producto_id)
    return render(request, "afterselling/opiniones.html",{'opiniones':opiniones,'producto':producto})

class Encuestas(View):
    def get(self,request,producto_id):
        id=producto_id
        carro = Carro(request)
        productos = list()
        for key, value in carro.carro.items():
            productos.append({'nombre':value['nombre'],'id':key})
        formulario_encuesta = EncuestaForm()
        return render(request, "afterselling/encuesta.html", {'forms_encuesta': formulario_encuesta,'ldp':productos,'producto_id':id})

    def post(self, request,producto_id):
        id=producto_id
        formulario_encuesta = EncuestaForm(data=request.POST)

        if formulario_encuesta.is_valid():
            formulario_encuesta.save()

        return render(request, "afterselling/pventa.html",{'producto_id':id})

