from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from .models import Cliente, Reserva

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','ultima_visita_con_reserva','reservas','notas' ]
    readonly_fields = ["ultima_visita_con_reserva",'reservas']
    search_fields = ['nombre','telefono']
    def reservas(self, obj):
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
    search_fields = ['cliente__nombre', 'cliente__telefono']
    list_display = ['cliente','fecha','comensales']
    list_filter =(('fecha',DateTimeRangeFilter),)
    date_hierarchy = 'fecha'