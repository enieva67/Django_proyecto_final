import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('SVG')
from servicios.models import Servicio, DataFrame, ClienteEstudio
from sklearn.cluster import KMeans
import os
from django.conf import settings
import seaborn as sns
sns.set_style('darkgrid')

class DataFrameServicios :

    def __init__(self, datos,fil,separador):
        self.tabla_datos=formato(datos,separador)
        self.dat = dict(self.tabla_datos.iloc[:fil, :])
        self.var=list(self.dat.keys())
        self.val=np.transpose(list(self.dat.values()))


    def calcular(self, nombre_de_funcion, datos):
        funcion=eval(nombre_de_funcion)
        datosn=datos.select_dtypes(include=np.number)
        return dict(np.round(funcion(datosn),2))

class DataFrameEstudios :

    def __init__(self, datos,fil,separador):
        self.tabla_datos=formato(datos,separador)
        self.dat = dict(self.tabla_datos.iloc[:, 2:])
        self.var=list(self.dat.keys())
        self.val=np.transpose(list(self.dat.values()))


def promedio(datos):
    return np.mean(datos, axis=0)

def maximo(datos):
    return np.max(datos, axis=0)

def varianza(datos):
    return np.var(datos, axis=0)

def minimo(datos):
    return np.min(datos, axis=0)

def std(datos):
    return np.std(datos, axis=0)


def formato(datos,separador):
    nombre = str(datos)
    suffix = ('.xlsx', '.xls')
    if nombre.endswith(suffix):
        tabla_datos = pd.read_excel(datos)
    else:
        tabla_datos = pd.read_csv(datos, sep=separador)
    return  tabla_datos

def df(datos):
    lista=[]
    for d in datos:
        lista.append([d.age,d.annual_income,d.spscore])
    return lista

def clustering(datos,cliente):
    clientes_db = pd.DataFrame(data=datos, columns=['edad', 'ingreso', 'gastos'])
    X=clientes_db.iloc[:, 1:].values
    kmeans = KMeans(n_clusters=5, init="k-means++", max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)
    numero=kmeans.predict([[cliente.annual_income, cliente.spscore]])[0]
    comentarios=[' cauto ',' estandard ',' objetivo ',' descuidado ','conservador ']
    # Visualización de los clusters
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100,alpha=0.75, c="red", label="Cautos")
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, alpha=0.75,c="blue", label="Estandard")
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100,alpha=0.75, c="green", label="Objetivo")
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100,alpha=0.75, c="cyan", label="Descuidados")
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100,alpha=0.75, c="magenta", label="Conservadores")
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c="yellow", label="Baricentros")
    plt.scatter(float(cliente.annual_income), float(cliente.spscore), s=130, c="black", label="Cliente")
    plt.title("Cluster de clientes : Es un cliente "+comentarios[numero])
    plt.xlabel("Ingresos anuales (en miles de $)")
    plt.ylabel("Puntuación de Gastos (1-100)")
    plt.legend()
    plt.savefig(os.path.join(settings.MEDIA_ROOT, "servicios/datos/imagenes/cluster_cliente"+str(cliente.id)+".png"))
    plt.close()
    return comentarios[numero]