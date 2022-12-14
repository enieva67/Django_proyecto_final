from django.shortcuts import render
from servicios.models import Servicio, DataFrame
from django.views import View

from .forms import EstadisticaForm
from .operaciones import DataFrameServicios


# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})


def probar(request,servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)
    archivos = DataFrame.objects.all()
    separador=[',',';']
    prueba='Probando el servicio de '+servicio.titulo
    return render(request, "servicios/grupos/"+servicio.tem, {"servicio": servicio,'prueba':prueba,'archivos':archivos,'separador':separador})

def mostrar_datos(request,archivo_id):
    archivo = DataFrame.objects.get(id=archivo_id)
    archivos = DataFrame.objects.all()
    prueba='Probando el servicio de '+archivo.nombre
    return render(request, "servicios/grupos/estadistica.html", {"archivo": archivo,'prueba':prueba,'archivos':archivos})

def mostrar_datos_tabla(request,archivo_id,separador):
    archivo = DataFrame.objects.get(id=archivo_id)
    contenido=archivo.datos
    id=archivo_id
    sep=[',',';']
    funcion=['promedio','varianza','maximo','minimo','std']
    datos=DataFrameServicios(contenido,17,separador)
    fdatos = {'variables': datos.var, 'datos': datos.val,'archivo_id':id,'separador':separador,'funcion':funcion,'archivo':archivo}
    return render(request,"servicios/grupos/cargar_archivo.html",fdatos)

def calcular(request,archivo_id,separador,funcion):
    archivo = DataFrame.objects.get(id=archivo_id)
    contenido = archivo.datos
    datos = DataFrameServicios(contenido, 17, separador)
    dat=datos.tabla_datos
    id=archivo_id
    funciones = ['promedio', 'varianza', 'maximo', 'minimo', 'std']
    resultado=datos.calcular(funcion,dat)
    fdatos = {'variables': resultado.keys(), 'datos': resultado.values(),'archivo_id':id,'separador':separador,'funcion':funciones}
    return render(request, "servicios/grupos/mostrar_resultados_analisis.html",fdatos)


class Formulario_de_estadistica (View):
    def get(self,request):

        formulario_est = EstadisticaForm()
        return render(request, "servicios/grupos/formulario.html", {'forms_est': formulario_est})

    def post(self, request):
        formulario_posts = EstadisticaForm(request.POST,request.FILES)

        if formulario_posts.is_valid():
            formulario_posts.save()

        archivos=DataFrame.objects.all()
        separador = [',', ';']
        return render(request, "servicios/grupos/estadistica.html", {'archivos':archivos,'separador':separador})
