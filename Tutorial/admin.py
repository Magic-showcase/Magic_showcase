from django.contrib import admin
from .models import Categoria,Tutorials
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria
    readonly_fields=('Created','Update')
    list_display=['Nombre']
    search_fields=('Nombre',)


class TotoAdmin(admin.ModelAdmin):
    model=Tutorials
    readonly_fields=('Created','Update')
    list_display=['Titulo','Autor','Categorias']
    search_fields=('Titulo','Autor')
    list_filter=('Titulo','Autor','Categorias','Created','Update')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tutorials,TotoAdmin)
