from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = PhoneNumberField(unique=True)
    notas = models.TextField(blank=True)

    def ultima_visita_con_reserva(self):
        return self.reservas.all().order_by('fecha').last().fecha

    def numero_de_visitas(self):
        return self.reservas.all().count()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey(to=Cliente,on_delete=models.CASCADE,related_name="reservas")
    fecha = models.DateTimeField(verbose_name="Fecha de la reserva")
    comensales = models.IntegerField(verbose_name="Numero de comensales")