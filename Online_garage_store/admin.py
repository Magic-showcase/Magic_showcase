from django.contrib import admin
from .models import User_Product
from .models import User_Envio
from .models import User_Venta
from .models import User_Venta_descrip
from .models import Vendedor
# Register your models here.
class Vendedoradmin(admin.ModelAdmin):
    model=Vendedor
    list_display=['Usuario','Sexo','Edad','Email','Domicilio']

class User_Productoadmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')
    list_display=['Nombre','Vendedor']

class User_Envioadmin(admin.ModelAdmin):
    model=User_Envio
    list_display=['Vendedor','Fecha','Entregado']
    #Filtrar informacion por campo
    list_filter=('Fecha','Entregado',)
    #detectar meses y años 
    date_hierarchy='Fecha'

class User_Venta_descrip_admin(admin.ModelAdmin):
    model=User_Venta_descrip
    list_display=['Vendedor','Cliente','Cantidad','Producto','Precio_unitario']
    list_filter=('Cliente','Producto')

class User_Venta_admin(admin.ModelAdmin):
    model=User_Venta
    list_display=['Vendedor','Venta_desc','Cliente','Costo_total']
    list_filter=('Cliente','Costo_total')
#Registro de table vendedor
admin.site.register(Vendedor,Vendedoradmin)
#
admin.site.register(User_Product,User_Productoadmin)
#Registro de table Envio
admin.site.register(User_Envio,User_Envioadmin)
#Registo de tabla Venta_descrp
admin.site.register(User_Venta_descrip,User_Venta_descrip_admin)
#Registro venta
admin.site.register(User_Venta,User_Venta_admin)