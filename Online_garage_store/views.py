from django.shortcuts import render
#importar Tienda,Productor
from .models import User_Product

def (request):
    #importar todos los productos
    articulo=User_Product.objects.all()
    return render(request,'Centro/Online_garage.html',{'articulo':articulo})