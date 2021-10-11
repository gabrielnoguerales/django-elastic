from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Producto, Categoria, Descuento

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.foto.url))


    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ['image_tag','titulo','precio_base' ]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.foto.url))


    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ['image_tag','titulo' ]


admin.site.register(Descuento)
