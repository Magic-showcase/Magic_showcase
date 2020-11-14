from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#importar Tienda,Productor
from Tienda.models import Producto
from Usuario.models import Users


@login_required(login_url='/Login/')
def Tienda(request):
    #importar todos los productos
    articulo=Producto.objects.all()
    return render(request,'Centro/Tienda.html',{'articulo':articulo})
