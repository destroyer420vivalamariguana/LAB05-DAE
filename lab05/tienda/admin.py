from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Producto
from .models import Cliente

# Acción personalizada para marcar como VIP
def marcar_como_vip(modeladmin, request, queryset):
    # Actualizar el campo 'es_vip' de los registros seleccionados
    queryset.update(es_vip=True)

marcar_como_vip.short_description = "Marcar como VIP"

# Registrar los modelos en el administrador
admin.site.register(Categoria)
admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Configuración de la administración de productos
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'mas_vendido']
    list_filter = ['categoria', 'mas_vendido']
    actions = ['marcar_como_mas_vendido']

    def marcar_como_mas_vendido(self, request, queryset):
        # Actualizar el campo 'mas_vendido' de los productos seleccionados
        queryset.update(mas_vendido=True)

    marcar_como_mas_vendido.short_description = 'Marcar como Más Vendido'

# Registrar el modelo Cliente y la acción personalizada en el administrador
admin.site.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion', 'es_vip']
    actions = [marcar_como_vip]  # Agregar la acción personalizada "Marcar como VIP"
