from django.contrib import admin

from .models import Cliente, Reserva

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Datos cliente", {
            'fields': ('nombre','telefono')
        }),
        ('Notas', {
            'classes': ('collapse',),
            'fields': ('notas',),
        }),
    )

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
    list_filter =('fecha',)
    date_hierarchy = 'fecha'
    fieldsets = (
        ("Datos de la reserva", {
            'fields': ('cliente','fecha','comensales')
        }),
        ('Notas de la reserva', {
            'classes': ('collapse',),
            'fields': ('notas',),
        }),
    )