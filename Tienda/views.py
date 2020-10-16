from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
#importar Tienda,Productor
from Tienda.models import Producto

def Tienda(request):
    #importar todos los productos
    articulo=Producto.objects.all()
    return render(request,'Centro/Tienda.html',{'articulo':articulo})
