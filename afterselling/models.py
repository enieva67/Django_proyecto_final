from django.db import models

# Create your models here.
from django.db import models

class Encuesta(models.Model):
    M = 'M'
    F = 'F'
    NB = 'N'

    GENERO_CHOICES = [
        (M, 'Masculino'),
        (F,'Femenino'),
        (NB, 'No binario'),

    ]
    genero = models.CharField(
        max_length=2,
        choices=GENERO_CHOICES ,
        default=F,
    )

    EXC = 'EXC'
    MB = 'MB'
    B = 'B'
    REG = 'REG'
    M = 'M'
    OPINION_PRODUCTO_CHOICES = [
        (EXC, 'Excelente'),
        (MB,'Muy bueno'),
        (B, 'Bueno'),
        (REG, 'Regular'),
        (M, 'Malisimo'),
    ]
    opinion = models.CharField(
        max_length=3,
        choices=OPINION_PRODUCTO_CHOICES ,
        default=B,
    )

    resenia=models.TextField(max_length=500)

    edades=models.IntegerField()

    PRIMARIO_I = 'PI'
    PRIMARIO_C = 'PC'
    SECUNDARIO_I = 'SI'
    SECUNDARIO_C = 'SC'
    UNIVERSITARIO_I = 'UI'
    UNIVERSITARIO_C = 'UC'
    POSTGRADO='PGR'

    ESTUDIOS_CHOICES = [
        (PRIMARIO_I, 'Primario incompleto'),
        (PRIMARIO_C, 'Primario completo'),
        (SECUNDARIO_I, 'Secundario incompleto'),
        (SECUNDARIO_C, 'Secundario completo'),
        (UNIVERSITARIO_I, 'Universitario incompleto'),
        (UNIVERSITARIO_C, 'Universitario completo'),
        (POSTGRADO,'Postgrado')
    ]
    estudios = models.CharField(
        max_length=3,
        choices=ESTUDIOS_CHOICES,
        default=SECUNDARIO_C,
    )
    producto = models.IntegerField(default=1)

