import numpy as np
from carro import context_processor


class Cuotas:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        self.capital = context_processor.importe_total_carro(request)["importe_total_carro"]

        self.TEA = 0
        cuotas = self.session.get("cuotas")

        if not cuotas:
            cuotas = self.session["cuotas"] = {'cantidad':1,'forma_de_pagar':'contado','monto_de_cuota':self.capital, 'TEA':0,'Descuento':0}

        self.cuotas = cuotas


    def cuota(self, V,n,i=0.75):
        if n==1:
            self.cuotas['monto_de_cuota']=V*(1-self.cuotas['Descuento'])
            self.guardar_cuotas()
            return
        if 3<n<=6:
            i=i+0.1
        elif 6<n<=12:
            i=i+0.15
        elif n>12:
            i=1+0.03*(n-12)
        TEA=i
        i=i/12
        if i > 0.5:
            i=np.round(i,2)
        C =np.round((V * (1+i)**n * i)/((1+i)**n-1),2)
        #self.cuotas['forma_de_pagar'] ='tarjeta'
        self.cuotas['monto_de_cuota']=np.round(C * (1-self.cuotas['Descuento']),2)
        self.TEA = TEA * 100
        self.cuotas['TEA']=self.TEA
        self.guardar_cuotas()


        return TEA

    def aumentar(self):
        self.cuotas['cantidad']+=1
        self.cuota(V=self.capital,n=self.cuotas['cantidad'])
        return

    def disminuir(self):
        self.cuotas['cantidad'] -= 1
        self.cuota(V=self.capital, n=self.cuotas['cantidad'])
        return

    def guardar_cuotas(self):
        self.session["cuotas"]=self.cuotas
        self.session.modified=True

