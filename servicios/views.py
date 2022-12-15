from django.shortcuts import render
from servicios.models import Servicio, DataFrame, ClienteEstudio,Estudio
from django.views import View

from .forms import EstadisticaForm, EstudioClienteForm
from .operaciones import DataFrameServicios,DataFrameEstudios,df,clustering


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

def mostrar_datos_db(request,archivo_id,separador):
    clientes_db=ClienteEstudio.objects.all()
    dat=df(clientes_db)
    #clustering(dat,1)
    #for d in datos.val:
        #ClienteEstudio.objects.create(age =int(d[0]),annual_income =int(d[1]), spscore=int(d[2]))
    fdatos = {'clientes_db':clientes_db,'dat':dat}
    return render(request,"servicios/grupos/clusters.html",fdatos)

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

class Formulario_clientes_db(View):
    def get(self,request):
        formulario_cliente_db = EstudioClienteForm()
        return render(request, "servicios/grupos/formulario_clientes_db.html", {'formulario_cliente_db': formulario_cliente_db })

    def post(self, request):
        clientes_db = ClienteEstudio.objects.all()
        dat = df(clientes_db)

        formulario_posts = EstudioClienteForm(request.POST)

        if formulario_posts.is_valid():
           cliente= formulario_posts.save()
           perfil=clustering(dat, cliente)

           estudio = Estudio.objects.create(perfil=perfil, imagen="servicios/datos/imagenes/cluster_cliente"+str(cliente.id)+".png")



        return render(request, "servicios/grupos/perfil.html", {'cliente':cliente,'estudio':estudio})