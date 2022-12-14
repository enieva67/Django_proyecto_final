from django.contrib import admin
from .models import Categoria, Post, Comentario

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)