from django.contrib import admin
from .models import Servicio, DataFrame, ClienteEstudio,Estudio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(DataFrame)
admin.site.register(ClienteEstudio)
admin.site.register(Estudio)