from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="servicios")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    tem = models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo

class DataFrame(models.Model):
    nombre =models.CharField(max_length=30)
    datos = models.FileField(upload_to ='servicios/datos')
    imagen = models.ImageField(upload_to="servicios", null=True, blank=True)
    class Meta:
        verbose_name='datos'
        verbose_name_plural='datos'

    def __str__(self):
        return self.nombre

        


