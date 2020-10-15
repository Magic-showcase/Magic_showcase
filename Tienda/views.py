from django.http import HttpResponse 
#Importar shortcuts
from django.shortcuts import render



def Tienda(request):
    return render(request,'Central/Tienda.html')
