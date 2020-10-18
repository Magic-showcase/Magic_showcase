from django.contrib import admin
from .models import Producto
from .models import Envio
# Register your models here.

class Productoadmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')

class Envioadmin(admin.ModelAdmin):
    model=Envio
    list_display=['Numero','Fecha','Entregado']
    #Filtrar informacion por campo
    list_filter=('Fecha','Entregado',)
    #detectar meses y años 
    date_hierarchy='Fecha'

admin.site.register(Producto,Productoadmin)
#Registro de table Envio
admin.site.register(Envio,Envioadmin)
