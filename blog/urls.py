from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Agregar_posts, Agregar_comentario

urlpatterns = [

    path('',views.blog, name="Blog"),
    path('<int:posts_id>/',views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('formulario/', Agregar_posts.as_view(), name="agregar_posts"),
    path('comentario/<int:posts_id>/',Agregar_comentario.as_view(), name="agregar_comentario"),
    path('mostrar/<int:posts_id>/',views.mostrar_comentarios, name="mostrar_comentario")

]