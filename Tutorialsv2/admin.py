from django.contrib import admin
from .models import Categoria, Tutoriales

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria
    readonly_fields=('Created','Update')
    list_display=['Nombre']
    search_fields=('Nombre',)


class TutorialAdmin(admin.ModelAdmin):
    model=Tutoriales
    readonly_fields=('Created','Update')
    list_display=['Titulo','Autor']
    search_fields=('Titulo','Autor')
    list_filter=('Titulo','Autor','Categorias',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tutoriales,TutorialAdmin)
