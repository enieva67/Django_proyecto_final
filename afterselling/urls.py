from django.urls import path

from . import views

from .views import Encuestas
urlpatterns = [

    path('pventa', views.pventa, name="pventa"),
    path('encuesta/<int:producto_id>/', Encuestas.as_view(), name="encuesta"),
    path('opinion/<int:producto_id>/', views.opinion, name="opinion"),
]