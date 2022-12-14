from django.urls import path

from .import views



urlpatterns = [

    path("", views.procesar_pedido, name="procesar_pedido"),
    path("comenzar_compra", views.comenzar_compra, name="comenzar_compra"),
    path("agregar_cuota", views.agregar_cuota, name="agregar_cuota"),
    path("disminuir_cuota", views.disminuir_cuota, name="disminuir_cuota"),
    path("tarjetas", views.tarjetas, name="tarjetas"),
    path("elegir/<int:tarjeta_id>", views.elegir, name="elegir"),
]



