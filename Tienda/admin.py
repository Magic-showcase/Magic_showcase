from django.contrib import admin
from .models import Producto
from .models import Envio
# Register your models here.
from .models import Venta
class Productoadmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')
    list_display=['Nombre']

class Envioadmin(admin.ModelAdmin):
    model=Envio
    list_display=['Fecha','Entregado']
    #Filtrar informacion por campo
    list_filter=('Fecha','Entregado',)
    #detectar meses y años 
    date_hierarchy='Fecha'


class Venta_admin(admin.ModelAdmin):
    model=Venta
    list_display=['Cliente','Costo_total']
    list_filter=('Cliente','Costo_total')

admin.site.register(Producto,Productoadmin)
#Registro de table Envio
admin.site.register(Envio,Envioadmin)

#Registro venta
admin.site.register(Venta,Venta_admin)