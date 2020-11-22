from django.contrib import admin
from .models import Producto
# Register your models here.
from .models import Venta
class Productoadmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')
    list_display=['Nombre','Seccion','Precio']
    list_filter=('Seccion','Created','Update')
class Venta_admin(admin.ModelAdmin):
    model=Venta
    list_display=['Cliente','Paypal_cliente','Producto','Costo_total']
    list_filter=('Cliente','Paypal_cliente','Producto','Costo_total','Created','Update')

admin.site.register(Producto,Productoadmin)
#Registro venta
admin.site.register(Venta,Venta_admin)