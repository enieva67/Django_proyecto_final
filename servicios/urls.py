from django.urls import path

from . import views
from .views import Formulario_de_estadistica

urlpatterns = [
   
    path('',views.servicios, name="Servicios"),
    path('probar/<int:servicio_id>/',views.probar, name="probar"),
    path('estadisticos/',Formulario_de_estadistica.as_view(), name="estadisticos"),
    path("mostrar_datos/<int:archivo_id>/", views.mostrar_datos, name="mostrar_datos"),
    path("mostrar_datos_tabla/<int:archivo_id>/<separador>/", views.mostrar_datos_tabla, name="mostrar_datos_tabla"),
    path('calcular/<int:archivo_id>/<separador>/<funcion>/',views.calcular, name="calcular"),
]



