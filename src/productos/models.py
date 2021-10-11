from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from comun.models import ImageModel


class Descuento(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    notas = models.TextField(blank=True,default="")
    porcentaje = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    acumulable = models.BooleanField(default=False)
    valor_fijo = models.IntegerField(default=0)
    codigo_descuento = models.CharField(max_length=100,blank=True)
    encontrable = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Categoria(ImageModel):
    CARPETA="Categoria"

    foto = models.ImageField(upload_to=CARPETA, blank=True)
    descuento = models.ForeignKey(Descuento,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Producto(ImageModel):
    CARPETA = "Producto"

    foto = models.ImageField(upload_to=CARPETA, blank=True)
    descripcion = models.TextField()
    precio_base = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuento,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo