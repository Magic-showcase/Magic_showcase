from django.contrib import admin
from .models import Producto

# Register your models here.

class Productoadmin(admin.ModelAdmin):
    readonly_fields=('Created','Update')

admin.site.register(Producto,Productoadmin)