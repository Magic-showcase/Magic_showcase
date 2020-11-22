from django.contrib import admin
from .models import Item,Showcase
# Register your models here.
class Itemadmin(admin.ModelAdmin):
    model=Item
    readonly_fields=('Created','Update')
    list_display=['Usuario','Nombre','Seccion','Precio']
    list_filter=('Usuario','Seccion','Created','Update')
class Showcaseadmin(admin.ModelAdmin):
    model=Showcase
    list_display=['Usuario','Nombrevi','Seccion']
    list_filter=('Usuario','Seccion','Created','Update')

admin.site.register(Item,Itemadmin)
#Registro vitrina
admin.site.register(Showcase,Showcaseadmin)
