from django.contrib import admin
from .models import Categoria,POST
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')

class POSTAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(POST,POSTAdmin)
