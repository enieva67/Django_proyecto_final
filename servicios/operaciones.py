import numpy as np
import pandas as pd


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