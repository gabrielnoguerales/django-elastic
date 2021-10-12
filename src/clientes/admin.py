from django.contrib import admin
# Register your models here.
from .models import Cliente, Reserva

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','ultima_visita_con_reserva','ver_reservas','notas' ]
    def ver_reservas(self, obj):
        from django.urls import reverse
        from django.utils.http import urlencode
        from django.utils.html import format_html
        url = (
                "/admin/clientes/reserva/"
                + "?"
                + urlencode({"cliente__id": f"{obj.id}"})
        )
        texto = 'reserva'
        if obj.numero_de_visitas() > 1:
            texto += 's'
        return format_html('<a href="{}">{} {}</a>', url, obj.numero_de_visitas(), texto)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente','fecha','comensales']